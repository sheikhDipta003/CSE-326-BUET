from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm   # Import the class containing our customized form instead of using the default one.

# creating register view
def register(request):
    # If the HttpRequest coming through 'register/' route is a POST request, then instantiate a form containing the POST data, otherwise
    # create just an empty form.
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # If POST request, validate credentials and provide feedback
        if form.is_valid():
            # Create a new user with the form data
            form.save()
            username = form.cleaned_data.get('username')    # Convert the username into proper Python type and return it
            # Provide feedback message
            messages.success(request, f'Account created for {username}, you will now be redirected to login page.')
            # Redirect user to login page
            return redirect('login')        # The 'name' attribute that we assigned to the 'login/' url in Harpy/urls.py
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})
