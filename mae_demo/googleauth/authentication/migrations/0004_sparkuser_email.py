# Generated by Django 2.1.7 on 2019-05-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20190501_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparkuser',
            name='email',
            field=models.CharField(default='No Email', max_length=100),
        ),
    ]
