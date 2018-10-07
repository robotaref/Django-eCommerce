from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login,get_user_model

def home_page(request):
    context={
        'title':"hello world",
        'content':'home page'
    }
    return render(request,"home_page.html",context)


def login_page(request):
    login_form=LoginForm(request.POST or None)

    context = {
        'title': "Login page",
        "form":  login_form

    }
    if request.user.is_authenticated:
        print('True')
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username=login_form.cleaned_data.get('username')

        email=login_form.cleaned_data.get('email')
        password=login_form.cleaned_data.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            context['form'] = login_form
        else:
            print('Error authenticating')
    else:
        print('invalid')
    if request.method == "POST":
        print(request.POST.get('email'))

    return render(request,"auth/login_page.html",context)


def register_page(request):
    register_form=RegisterForm(request.POST or None)

    context = {
        'title': "Login page",
        "form":  register_form

    }
    User=get_user_model()
    if register_form.is_valid():
        username=register_form.cleaned_data.get('username')
        email=register_form.cleaned_data.get('email')
        password=register_form.cleaned_data.get('password')

        new_user=User.objects.create_user(username=username,email=email,password=password)
        print(new_user)
    return render(request,"auth/register_page.html",context)


def register_food_page(request):
    return render(request,"home_page.html",{})
