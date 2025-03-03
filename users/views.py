from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm


from rest_framework_simplejwt.tokens import RefreshToken

from .forms import LoginForms, SignupForms ,UpdatePersonalInfoForms, UpdatePassword
from .models import User



def login_signup(reqeust):
    return render(reqeust, "signup_login.html")


def login_view(request):

    if request.method == 'POST':

        # sending request.POST data into form
        form = LoginForms(request.POST)

        if form.is_valid():

            # get username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # authenticate user into that  exist in the database.
            user = authenticate(request, username=username, password=password)

            if user:

                ### An example
                ## 1. authenticate checks whether "ali" and "1234" are valid.
                ## 2. If true, login will cause request.user.username to be equal to "ali" in the application from now on, and the user will be recognized as logged in.

                # It actually logs the user into the system and activates the session for them.
                login(request, user)

                refresh = RefreshToken.for_user(user)


                # Save access token in access_token session name
                request.session['access_token'] = str(refresh.access_token)

                # Save refresh token in refresh_token session name
                request.session['refresh_token'] = str(refresh)

                # Save relevant messages in the session for use in a html file
                # because with redirect we can't send message ( into html file )
                request.session['username'] = username
                #request.session['msg'] = "welcome"

                return redirect('/')
            else:
                return render(request, 'signup_login.html', {"msg_error" : "username or password is wrong!"})


#
def protected_view(request):
    # Get access_token ( that we save in session in login_view function) from session with name access_token.
    access_token = request.session.get('access_token')

    # If the token had been invalidated go to auth page.
    if not access_token:
        return redirect('auth')

    return render(request, 'index.html', {"msg" : ""})

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForms(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForms()

    return render(request,'signup_login.html',{'form':form})




def update_personal_info(request):
    if request.method == 'GET':
        return render(request, "user_panel.html")
    if request.method == 'POST':

        form = UpdatePersonalInfoForms(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return render(request, "user_panel.html", {"msg_p1" : "Your information was successfully registered."})
        else:

            return render(request, 'user_panel.html', {'form_info': form.errors})


def update_password(request):
    if request.method == 'POST':

        form = UpdatePassword(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()

            update_session_auth_hash(request, request.user)

            return render(request, "user_panel.html", {"msg_p2" : "Your information was successfully registered."})
        else:
            return render(request, 'user_panel.html', {'form_pass': form.errors})

def emailcheck(request):
    email_inp = request.POST.get('forgotEmail')

    user_exists = User.objects.filter(email=email_inp).exists()

    if user_exists:
        # email send function...
        token = get_random_string(length=32)

        request.session['token'] = token

        reset_link = request.build_absolute_uri(
            reverse('restpass', kwargs={'token': token})
        )
        subject = "Request to change password"
        message = f"Hello, please click this link to change your password: {reset_link}"
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [email_inp]

        request.session['email_user'] = email_inp

        send_mail(subject, message, email_form, recipient_list, fail_silently=False)


        # not complete yet...
        return render(request, "signup_login.html", {"em_not" : "Please check your email"})
    else:
        return render(request, "signup_login.html", {"em_not" : "User not found!"})


def rest_pass_view(request, token):
    session_token = request.session.get('token')

    if request.method == 'GET':  # for GET request
        return render(request, 'rest_password.html', {'token': token})
    elif request.method == 'POST':

        if session_token == token:
            try:
                user_email = request.session.get('email_user')
                user = User.objects.get(email=user_email)


                form = SetPasswordForm(user, request.POST)
                if form.is_valid():
                    form.save()
                    del request.session['token']
                    del request.session['email_user']
                    return redirect('home')
                else:
                    return render(request, 'rest_password.html', {'form': form.errors, 'token': token})
            except User.DoesNotExist:
                return render(request, 'rest_password.html', {'em_not': 'User not found!', 'token':token})
        else:
            return render(request, 'signup_login.html', {'em_not': 'Invalid or expired link!', 'token':token})


def delete_account(request):

    if request.method == 'POST':
        user = User.objects.filter(username=request.session['username'])

        if user:
            user.delete()
            logout(request)
            return redirect('home')
        else:
            return render(request, 'user_panel.html', {"error" : "we have problem"})

    else:
        return render(request, 'user_panel.html', {"error": "we have problem"})





