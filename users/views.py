from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from rest_framework_simplejwt.tokens import RefreshToken

from .forms import LoginForms, SignupForms ,UpdatePersonalInfoForms



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
                request.session['msg'] = "welcome"

                return redirect('/')


#
def protected_view(request):
    # Get access_token ( that we save in session in login_view function) from session with name access_token.
    access_token = request.session.get('access_token')

    # If the token had been invalidated go to auth page.
    if not access_token:
        return redirect('auth')

    return render(request, 'index.html', {"msg" : "welcome"})

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForms(request.POST)

        print("password form : ")
        print('form : ////////////////////// : ')

        print('form is valid : /////////////////// : ', form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print("errors from forms : ///////////////////// : ", form.errors)
    else:
        form = SignupForms()

    return render(request,'signup_login.html',{'form':form})



def user_panel(request):
    return render(request, "user_panel.html")


def update_personal_info(request):
    if request.method == 'POST':

        form = UpdatePersonalInfoForms(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return render(request, "user_panel.html", {"msg_p" : "Your information was successfully registered."})
        else:
            form = UpdatePersonalInfoForms(instance=request.user)

        return render(request, 'update_profile.html', {'form': form})





