from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken



# I create a function for login and signup
def login_view(request):
    if request.method == "post":

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': user.username
            })
        else:
            return Response({"error" : 'Invalid credentials'}, status=400)

        # when from type is login do this...
        if form_type == "login":
            user = authenticate(username=username, password=password)
            # what is in user
            print("user /////////////// : ", user)

            if user:
                login(request, user)

                # redirect to home page (main page)
                return redirect('home')
            else:
                return render(request, 'signup_login.html', {'error': 'Invalid credentials'})
        return render("index.html")


def signup_login(req):
    return render(req,'signup_login.html')

# Create your views here.

