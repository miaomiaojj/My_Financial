from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User,UserInfo
from .forms import CHOICES

def index(request):
    return render(request, 'register/index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    passwd=request.POST['password'].encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(passwd, salt)

    if (User.objects.filter(email=request.POST['email']).exists()):
        print('user exist')
        return render(request, 'register/index.html',{'RegisterMassage': "User exist, please login or register new account"} )

    else:
        print("hashed_password:",hashed_password)
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                                   password=hashed_password, email=request.POST['email'])
        user.save()
        request.session['id'] = user.id
        print('new user')
        return render(request, 'register/index.html',{'RegisterMassage': "Account create successful, please login"})


def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        passwd = request.POST['login_password'].encode()
        print("1111:,",passwd)
        n=len(user.password.encode())-1
        print("2222:,", user.password.encode()[2:n])

        if bcrypt.checkpw(passwd, user.password.encode()[2:n]):

            print("login success")
            request.session['id'] = user.id
            return redirect('/success')
        else:
            print("login fail")
            return redirect('/')


def success(request):
    user = User.objects.get(id=request.session['id'])

    context = {
        "user": user,
      #  "hidden":"hidden"

    }

    #return render(request, 'name_of_page.html', {'form': form})
    return render(request, 'register/success.html',context)





def userinfocollect(request):
    print("UserInfoCollect")
   # user = User.objects.get(id=request.session['id'])
    user = User.objects.get(id=request.session['id'])
    print(user.email)
    print(request.POST['othersMonthlyspend'])

    userInformation = UserInfo.objects.create(email=user,age=request.POST.get('age'),
                                              education=request.POST.get("education"), location=request.POST.get("location"),
                                              houseInfo=request.POST.get("houseInfo"),
                                              Maritalstatus=request.POST.get("Maritalstatus"),
                                              Occupation=request.POST.get("Occupation"),
                                              monthySalary=request.POST['monthySalary'],
                                              OtherMonthlyIncome=request.POST['OtherMonthlyIncome'],
                                              SavingBalance=request.POST['SavingBalance'],
                                              Investment=request.POST['Investment'], Property=request.POST['Property'],
                                              CreditCardLiabilities=request.POST['CreditCardLiabilities'],
                                              HomeMortgage=request.POST['HomeMortgage'],
                                              OtherLoan=request.POST['OtherLoan'], Foodspend=request.POST['Foodspend'],
                                              clothingspend=request.POST['clothingspend'],
                                              shopping=request.POST['shopping'],
                                              accommodation=request.POST['accommodation'],
                                              Transport=request.POST['Transport'],
                                              othersMonthlyspend=request.POST['othersMonthlyspend'])
    userInformation.save()
    request.session['id'] = userInformation.id


    monthly_Income = float(request.POST['monthySalary']) + float(request.POST['OtherMonthlyIncome'])
    monthly_Expense = float(request.POST['Foodspend']) + float(request.POST['clothingspend']) + float(request.POST['shopping']) + float(request.POST['accommodation']) + float(
        request.POST['Transport']) + float(request.POST['othersMonthlyspend'])
    monthly_Balance = monthly_Income - monthly_Expense
    Asset = float(request.POST['SavingBalance']) + float(request.POST['Investment']) + float(request.POST['Property'])
    liabilities = float(request.POST['CreditCardLiabilities']) + float(request.POST['HomeMortgage']) + float(request.POST['OtherLoan'])
    Networth = Asset - liabilities

    print(float(monthly_Income))
    print(float(monthly_Expense))
    print(float(monthly_Balance))
    print(float(Asset))
    print(float(Networth))

    if (monthly_Balance < 0.4 * monthly_Income):
        Summary1="reduce monthly expense,check which part excess budget"
    elif (monthly_Balance >= 0.4 * monthly_Income):
        Summary1= "Add 30% Monthly balance to saving account or investment, 10% Monthly balance used to cash reserve "
    if (liabilities > 0.5 * Asset):
        Summary2= "reduce long term liabilities smaller than 50% Asset, short term liabilities smaller than 20% of asset"
    elif (Networth < 0):
        Summary2="Assess your ability to service your debts"



    context = {
        "InfoSaveMassage": "Infomation updated",

        "MonthlyState":"Monthly Statement",
        "MonthlyIncome":"Monthly Income:",
        "Num_monthly_Income":monthly_Income,
        "MonthlyExpense":"MonthlyExpense:",
        "Num_MonthlyExpense": monthly_Expense,
        "MonthlyBalance": "Monthly Balance:",
        "Num_MonthlyBalance": monthly_Balance,

        "Personal_balance_statement": "Personal balance statement",
        "Asset":"Asset:",
        "Num_Asset": Asset,
        "liabilities":"liabilities:",
        "Num_liabilities": liabilities,
        "Networth": "Networth:",
        "Num_Networth": Networth,
        "Suggestion": "Suggestion:",
        "Summary1": Summary1,
        "Summary2": Summary2,
        "GoFactorAnalysis":"Factor effect Financial Statement Analysis"

    }


    return render(request, 'register/success.html', context)



def FactorAnalysis(request):
    Dataset_list = {"AdultDateset"}
    context = {
        'rest_list': Dataset_list
    }
    return render(request, 'register/FactorAnalysis.html', context)
