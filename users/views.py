from django.shortcuts import render, redirect
from .forms import LoginForms
from django.contrib.auth import authenticate, login

from rest_framework_simplejwt.tokens import RefreshToken

def login_signup(reqeust):
    return render(reqeust, "signup_login.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            print("This is user ///////////////////////// /////////// : ", user)

            if user:
                login(request, user)

                refresh = RefreshToken.for_user(user)
                print("refresh //////////////////// : /////////// ", refresh)


                request.session['access_token'] = str(refresh.access_token)
                request.session['refresh_token'] = str(refresh)

                return render(request, 'index.html', {"msg" : "welcome"})


def protected_view(request):
    access_token = request.session.get('access_token')

    if not access_token:
        return redirect('auth')

    return render(request, 'index.html', {"msg" : "welcome"})