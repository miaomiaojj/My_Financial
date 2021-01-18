from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class UserInfoManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['age']) == 0:
            errors['age'] = "please enter correct age"

        if (postData['education']) == 0:
            errors['education'] = "please enter correct education level"

        if (postData['location']) == 0:
            errors['location'] = "please enter correct location"
        if (postData['houseInfo']) == 0:
            errors['houseInfo'] = "please enter correct houseInfo"
        if (postData['Maritalstatus']) == 0:
            errors['Maritalstatus'] = "please enter correct Marital status "
        if (postData['Occupation']) == 0:
            errors['Occupation'] = "please enter correct Occupation"
        if (postData['monthySalary']) == 0:
            errors['monthySalary'] = "please enter correct monthySalary"
        if (postData['OtherMonthlyIncome']) == 0:
            errors['OtherMonthlyIncome'] = "please enter correct Other Monthly Income"
        if (postData['SavingBalance']) == 0:
            errors['SavingBalance'] = "please enter correct Saving Balance"
        if (postData['Investment']) == 0:
            errors['Investment'] = "please enter correct Investment"
        if (postData['Property']) == 0:
            errors['Property'] = "please enter correct Property"
        if (postData['CreditCardLiabilities']) == 0:
            errors['CreditCardLiabilities'] = "please enter correct Credit Card Liabilities"
        if (postData['HomeMortgage']) == 0:
            errors['HomeMortgage'] = "please enter correct HomeMortgage"
        if (postData['Other Loan']) == 0:
            errors['Other Loan'] = "please enter correct Other Loan"
        if (postData['Foodspend']) == 0:
            errors['Foodspend'] = "please enter correct Food spend"
        if (postData['clothingspend']) == 0:
            errors['clothingspend'] = "please enter correct clothing spend"
        if (postData['shopping']) == 0:
            errors['shopping'] = "please enter correct shopping"
        if (postData['accommodation']) == 0:
            errors['accommodation'] = "please enter correct accommodation"
        if (postData['Transport']) == 0:
            errors['Transport'] = "please enter correct Transport"
        if (postData['othersMonthlyspend']) == 0:
            errors['othersMonthlyspend'] = "please enter correct others Monthly spend"


        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class UserInfo(models.Model):
    email=models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    houseInfo = models.CharField(max_length=255)

    Maritalstatus = models.CharField(max_length=255)
    Occupation = models.CharField(max_length=255)
    monthySalary = models.CharField(max_length=255)
    OtherMonthlyIncome = models.CharField(max_length=255)
    SavingBalance = models.CharField(max_length=255)
    Investment = models.CharField(max_length=255)
    Property = models.CharField(max_length=255)
    CreditCardLiabilities = models.CharField(max_length=255)
    HomeMortgage = models.CharField(max_length=255)
    OtherLoan = models.CharField(max_length=255)
    Foodspend = models.CharField(max_length=255)
    clothingspend = models.CharField(max_length=255)
    shopping = models.CharField(max_length=255)
    accommodation = models.CharField(max_length=255)
    Transport = models.CharField(max_length=255)
    othersMonthlyspend = models.CharField(max_length=255)
    #objects = UserManager()

