from django.shortcuts import render
from django.shortcuts import redirect

from .models import Event
from .forms import EventCreateForm
from authentication.models import SparkUser


def event_index(request):
    sparkuser = SparkUser.objects.get(user=request.user)
    event_list = Event.objects.all()
    context = {'event_list': event_list, 'rsvped_event_list': sparkuser.event_set.all()}
    return render(request, 'event/event_index.html', context)


def create_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print("form post request done")
        form = EventCreateForm(request.POST, request.FILES or None)
        # check whether it's valid:
        print("form. is_valid done")
        if form.is_valid():
            # Grab the form data
            print("1st field done")
            name = form.cleaned_data['name']
            print("2nd field done")
            loc = form.cleaned_data['location']
            print("3rd field done")
            s_time = form.cleaned_data['start_time']
            print("4th field done")
            e_time = form.cleaned_data['end_time']
            image = form.cleaned_data['image']

            # Create and save a new event object
            e = Event(name=name, start_time=s_time,
                      end_time=e_time, location=loc, image=image)
            e.save()

        # Filled the form out incorrectly..
        else:
            for k in form.errors:
                print(k + form.errors[k])
            request.method = "GET"
            return create_event(request)

        # Redirect user to see all the events.
        return event_index(request)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventCreateForm()

    return render(request, 'event/event_form.html', {'form': form})

# Called when Going/Not Going button is clicked on the Event page.
def update_participants(request, event_id):
    s = SparkUser.objects.get(user=request.user)
    e = Event.objects.get(id=event_id)
    if e in s.event_set.all():
        e.participants.remove(s)
    else:    
        e.participants.add(s)
    e.save()
    # CHANGE WHEN DEPLOYING! 
    return redirect('http://127.0.0.1:8000/event/index')

