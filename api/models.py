from django.db import models

class Profiles(models.Model):
    profile_choice = (
        ('Self', 'Self'),
        ('Son', 'Son'),
        ('Daughter', 'Daughter'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
        ('Niece', 'Niece'),
        ('Nephew', 'Nephew'),
        ('Cousion', 'Cousion'),
        ('Friend', 'Friend'),
    )
    creating_profile_for = models.CharField(max_length=8, blank=True, null=True, choices=profile_choice)
    firstname = models.CharField(max_length=20, blank=False)
    middlename = models.CharField(max_length=20, blank=True)
    lastname = models.CharField(max_length=20, blank=False)
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, blank=True, null=True, choices=gender_choice)
    contact = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100, unique=True)
    confirm = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.firstname


