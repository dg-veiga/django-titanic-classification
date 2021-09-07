from django.db import models

# Create your models here.
class TitanicTest(models.Model):
    passengerid = models.AutoField(primary_key=True, db_column='PassengerId', blank=False, null=False)  # Field name made lowercase.
    survived = models.BigIntegerField(db_column='Survived', blank=True, null=True)  # Field name made lowercase.
    pclass = models.BigIntegerField(db_column='Pclass', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    sex = models.TextField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sibsp = models.BigIntegerField(db_column='SibSp', blank=True, null=True)  # Field name made lowercase.
    parch = models.BigIntegerField(db_column='Parch', blank=True, null=True)  # Field name made lowercase.
    ticket = models.TextField(db_column='Ticket', blank=True, null=True)  # Field name made lowercase.
    fare = models.TextField(db_column='Fare', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cabin = models.TextField(db_column='Cabin', blank=True, null=True)  # Field name made lowercase.
    embarked = models.TextField(db_column='Embarked', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'titanic_test'


class TitanicTrain(models.Model):
    passengerid = models.AutoField(primary_key=True, db_column='PassengerId', blank=False, null=False)  # Field name made lowercase.
    survived = models.BigIntegerField(db_column='Survived', blank=True, null=True)  # Field name made lowercase.
    pclass = models.BigIntegerField(db_column='Pclass', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    sex = models.TextField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sibsp = models.BigIntegerField(db_column='SibSp', blank=True, null=True)  # Field name made lowercase.
    parch = models.BigIntegerField(db_column='Parch', blank=True, null=True)  # Field name made lowercase.
    ticket = models.TextField(db_column='Ticket', blank=True, null=True)  # Field name made lowercase.
    fare = models.TextField(db_column='Fare', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cabin = models.TextField(db_column='Cabin', blank=True, null=True)  # Field name made lowercase.
    embarked = models.TextField(db_column='Embarked', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'titanic_train'