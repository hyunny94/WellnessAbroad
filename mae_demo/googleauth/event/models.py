from django.db import models

# Create your models here.
from authentication.models import SparkUser

# Not used.. But I don't know how to get rid of this. 
# Deleting this will cause errors. 
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'data/{0}/{1}'.format(instance.id, filename)


class Event(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=30)
    image = models.FileField(upload_to='images/',
                             default='data/jisungpark1.jpg')
    participants = models.ManyToManyField(SparkUser)
