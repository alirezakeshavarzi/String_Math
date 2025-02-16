from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



# I create a function for login and signup
def auth_view(request):
    if request.method == "post":
        # I don't know what is form_type.
        form_type = request.post.get("form_type")

        # get email and password from user ( in field )
        email = request.post["email"]
        password = request.post["password"]

        # when from type is login do this...
        if form_type == "login":
            user = authenticate(username=email, password=password)
            # what is in user
            print("user /////////////// : ", user)

            if user:
                login(request, user)

                # redirect to home page (main page)
                return redirect('home')
            else:
                return render(request, 'signup_login.html', {'error': 'Invalid credentials'})
        return render("index.html")


# Create your views here.

