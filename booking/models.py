from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


DOCTOR_CHOICES = (
    ('doctor1', 'Doctor1'),
    ('doctor2', 'Doctor2'),
    ('doctor3', 'Doctor3'),
)
TIME_CHOICES = (
    ('07:00-08:00', '07:00-08:00'),
    ('08:00-09:00', '08:00-09:00'),
    ('09:00-10:00', '09:00-10:00'),
    ('10:00-11:00', '10:00-11:00'),
    ('11:00-12:00', '11:00-12:00'),
    ('13:00-14:00', '13:00-14:00'),
    ('14:00-15:00', '14:00-15:00'),
    ('15:00-16:00', '15:00-16:00'),
    ('16:00-17:00', '16:00-17:00'),
)


class BookModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=30)
    email = models.EmailField()
    doctor = models.CharField(
        max_length=10, choices=DOCTOR_CHOICES, default='doctor1')
    message = models.TextField(max_length=300)
    time = models.CharField(
        max_length=15, choices=TIME_CHOICES, default='07:00-08:00')
    date = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.name
