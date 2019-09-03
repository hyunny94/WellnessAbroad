from django import forms
from django.contrib.admin import widgets
import datetime


class ProfileForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,
    						widget = forms.TextInput(
           					attrs = {'style': 'width: 30%; height:30px; border-radius: 5px'
                					 }
        					))
    image = forms.ImageField(label="Image")
    email = forms.CharField(label= "Email",
							widget = forms.TextInput(
			           		attrs = {'style': 'width: 30%; height:30px; border-radius: 5px'
			             			}
						))
    age =forms.CharField(label= "Age",
							widget = forms.TextInput(
			           		attrs = {'style': 'width: 30%; height:30x; border-radius: 5px'
			                		}
						))

    gender = forms.CharField(label="Gender",widget = forms.TextInput(
			           		attrs = {'style': 'width: 30%; height:30px; border-radius: 5px'
			                			}
						))
    interest =  forms.CharField(label="Interest",
							widget = forms.TextInput(
			           		attrs = {'style': 'width: 30%; height:30px; border-radius: 5px'
			                			}
						))

class ProfileNameForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,
    						widget = forms.TextInput(
           					attrs = {'style': 'width: 60%; height:45px; border-radius: 10px'
                					}
        					))

class ProfileImageForm(forms.Form):
    image = forms.ImageField(label="Image")

class ProfileEmailForm (forms.Form): 
	email = forms.CharField(label= "Email",
							widget = forms.TextInput(
			           		attrs = {'style': 'width: 60%; height:45px; border-radius: 10px',
			                			'placeholder': 'This Field is Required'}
						))

class ProfileAgeForm(forms.Form):
    age = forms.IntegerField(label="Age",  
    						widget = forms.TextInput(
			           		attrs = {'style': 'width: 60%; height:45px; border-radius: 10px',
			                			'placeholder': 'This Field is Required'}
						))

class ProfileGenderForm(forms.Form):
    gender = forms.CharField(label="Gender",widget = forms.TextInput(
			           		attrs = {'style': 'width: 60%; height:45px; border-radius: 10px',
			                			'placeholder': 'This Field is Required'}
						))


class ProfileInterestForm (forms.Form): 
	interest = forms.CharField(label="Interest",
							widget = forms.TextInput(
			           		attrs = {'style': 'width: 60%; height:45px; border-radius: 10px',
			                			'placeholder': 'This Field is Required'}
						))

