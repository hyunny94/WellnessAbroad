from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import SparkUser
from .forms import ProfileForm, ProfileAgeForm, ProfileNameForm, ProfileEmailForm, ProfileGenderForm, ProfileImageForm, ProfileInterestForm
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        try:
            sparkuser = SparkUser.objects.get(user=request.user)
            print("the spark user is not yet created for this user.")

        except:
            sparkuser = SparkUser(user=request.user, profile_filled=False, email="null", age=100, gender="neutral")
            sparkuser.save()
            print("the spark user is now created for this user.")

        finally:
            sparkuser = SparkUser.objects.get(user=request.user)
            if sparkuser.profile_filled:
                return render(request, 'authentication/home.html')
            else:
                return create_profile(request)
    else:
        return render(request, 'authentication/index.html')


def create_profile(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST, request.FILES or None)
        # check whether it's valid:
        if form.is_valid():
            # Grab the form data
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            interest = form.cleaned_data['interest']

            # Create and save a new event object
            sparkuser = SparkUser.objects.get(user=request.user)
            sparkuser.name = name
            sparkuser.image = image
            sparkuser.email = email
            sparkuser.age = age
            sparkuser.gender = gender 
            sparkuser.interest = interest
            sparkuser.profile_filled = True
            try: 
                sparkuser.save(update_fields=["name", "profile_filled",\
                'image', 'email', 'age','gender', 'interest'])
            except:
                messages.error(request, 'Please fill the profile fully and correctly!')
                request.method = "GET"
                return create_profile(request)

        # Filled the form out incorrectly..
        else:
            for k in form.errors:
                print(k + form.errors[k])
            request.method = "GET"
            return create_profile(request)

        # Redirect user to the homepage!
        return index(request)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()

    return render(request, 'authentication/profile_form.html', {'form': form})


def view_profile(request):
    profile = SparkUser.objects.get(user_id=request.user.id)
    context = {'user': profile}
    return render(request, 'authentication/profile.html', context)

def edit_profile(request, item):
    print(item)
    # Get the current user 
    sparkuser = SparkUser.objects.get(user=request.user)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if item == "name":
            print ('name form!')
            form = ProfileNameForm(request.POST or None)
        elif item == 'email': 
            print ('email form!')
            form = ProfileEmailForm(request.POST or None)
        elif item == 'age':
            print ('age form!')
            form = ProfileAgeForm(request.POST or None)
        elif item == 'gender':
            print ('gender form!')
            form = ProfileGenderForm(request.POST or None)
        elif item == "interest": 
            print ('interest form!')
            form = ProfileInterestForm(request.POST or None)
        else: # image!
            print ('image form!')
            form = ProfileImageForm(request.POST, request.FILES or None)
        # check whether it's valid:
        if form.is_valid():
            # Grab the form data
            new = form.cleaned_data[item]

            # Update the sparkuser object
            if item == "name":
                sparkuser.name = new
                sparkuser.save(update_fields=["name"])
            elif item == 'email':
                sparkuser.email = new
                sparkuser.save(update_fields=['email'])
            elif item == 'age':
                sparkuser.age = new
                sparkuser.save(update_fields=['age'])
            elif item == 'gender':
                sparkuser.gender = new 
                sparkuser.save(update_fields=['gender'])
            elif item == 'interest': 
                sparkuser.interest = new
                sparkuser.save(update_fields=['interest'])
            else: # Image!
                sparkuser.image = new
                sparkuser.save(update_fields=['image'])

        # Filled the form out incorrectly..
        else:
            for k in form.errors:
                print(k + form.errors[k])
            request.method = "GET"
            return edit_profile(request, item)

        # Redirect user to the homepage!
        return view_profile(request)

    # if a GET (or any other method) we'll create a blank form
    else:
        if item == "name":
            form = ProfileNameForm(request.POST)
        elif item == 'email': 
            form = ProfileEmailForm(request.POST)
        elif item == 'age':
            form = ProfileAgeForm(request.POST)
        elif item == 'gender':
            form = ProfileGenderForm(request.POST)
        elif item == 'interest': 
            form = ProfileInterestForm(request.POST)
        else: #image!
            form = ProfileImageForm(request.POST, request.FILES or None)

    return render(request, 'authentication/edit_profile.html', {'form': form, 'item':item, 'user':sparkuser})


def about(request):
    return render(request, 'authentication/about.html')
