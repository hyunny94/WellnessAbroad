from django import forms
from django.contrib.admin import widgets
import datetime


class EventCreateForm(forms.Form):
    name = forms.CharField(label='Event Name', max_length=100,
                            widget = forms.TextInput(
                            attrs = {'style': 'width: 30%; height:35px; border-radius: 5px'
                                    }
                        ))
    location = forms.CharField(label='Event Location', max_length=100,
                                widget = forms.TextInput(
                                attrs = {'style': 'width: 30%; height:35px; border-radius: 5px'
                                        }
                            ))
    start_time = forms.SplitDateTimeField(label='Start Time', 
                            widget=widgets.AdminSplitDateTime(
                            attrs = {'style': 'width: 30%; height:35px; border-radius: 5px'
                                    }
                        ))
    end_time = forms.SplitDateTimeField(label='End Time', 
                            widget=widgets.AdminSplitDateTime(                            
                            attrs = {'style': 'width: 30%; height:35px; border-radius: 5px'
                                                    }
                                        ))
    image = forms.ImageField(label="Image")



