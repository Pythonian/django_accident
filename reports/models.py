from django.db import models
from django.urls import reverse


class TypeOfRoad(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AccidentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Report(models.Model):
    SUBMITTED = 'S'
    INVESTIGATION = 'I'
    CLOSED = 'C'
    STATUS_CHOICES = (
        (SUBMITTED, 'Submitted'),
        (INVESTIGATION, 'Investigation'),
        (CLOSED, 'Closed'),
    )
    witness_name = models.CharField(max_length=255)
    witness_email = models.EmailField()
    witness_phonenumber = models.CharField(max_length=18, blank=True, null=True)
    date_of_accident = models.DateField()
    time_of_accident = models.TimeField()
    is_fatal = models.BooleanField()
    image = models.ImageField(upload_to='reports')
    video = models.FileField(upload_to='videos', blank=True, null=True)
    accident_type = models.ForeignKey(AccidentType, on_delete=models.CASCADE)
    witness_involvement = models.BooleanField('Were you involved?')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=SUBMITTED)
    number_of_vehicles_involved = models.PositiveIntegerField()
    number_of_injured_victims = models.PositiveIntegerField(blank=True, null=True)
    number_of_deaths = models.PositiveIntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    type_of_road = models.ForeignKey(TypeOfRoad, on_delete=models.CASCADE)
    cause_of_accident = models.CharField(max_length=255)
    description = models.TextField('Describe what happened')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Accident report by {self.witness_name} on {self.date_of_accident}'

    def get_absolute_url(self):
        return reverse('report', kwargs={'id': self.id})
    