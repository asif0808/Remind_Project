from django.db import models
class Remind(models.Model):
    Reminder_methods=[('email','Email'),('sms','SMS')]
    date=models.DateField()
    time=models.TimeField()
    message=models.TextField()
    method=models.CharField(max_length=10,choices=Reminder_methods)
