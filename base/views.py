from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import TitanicTrain
from .serializers import TitanicTrainSerialized

import json
import numpy as np
import pandas as pd
import pickle
import sklearn

models_folder = settings.STATIC_DIR + '/ml_model'
loaded_model = pickle.load(open(models_folder + '/clf_model.sav', 'rb'))
loaded_pca = pickle.load(open(models_folder + '/pca_transf.sav', 'rb'))
loaded_ct = pickle.load(open(models_folder + '/column_transf.sav', 'rb'))

# Create your views here.
@api_view(['GET'])
def index(request):
    if request.method == 'GET':

        train_data = get_all_train_data()
        
        return render(request, 'main.html', {'title': 'Titanic - Survivors', 'train_data': train_data})

def get_all_train_data():
    train_data = TitanicTrain.objects.all()

    train_data_serialized = TitanicTrainSerialized(train_data[:], many=True)

    return train_data_serialized.data 

@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        # not used columns = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'Survived']
        # used columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
        # model.predict()

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        train_data = {
            'Pclass': [body['pclass']],
            'Sex': [body['sex']],
            'Age': [body['age']],
            'SibSp': [body['sibsp']],
            'Parch': [body['parch']],
            'Fare': [body['fare']],
            'Embarked': [body['embarked']],
        }

        train_data_df = pd.DataFrame(train_data)

        ct_transf = loaded_ct.transform(train_data_df)
        pca_transf = loaded_pca.transform(ct_transf)

        prediction = loaded_model.predict(pca_transf)[0]

        return JsonResponse({'Prediction': int(prediction)}, safe=True)