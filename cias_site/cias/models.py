from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Coach(models.Model):
    deviceID = models.IntegerField()
    name = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=10)
    emailAddress = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class MedicalStaff(models.Model):
    deviceID = models.IntegerField()
    name = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=10)
    emailAddress = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    hardwareID = models.IntegerField()
    emergencyContact = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class ImpactEvent(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    severity = models.IntegerField()
    timestamp = models.DateTimeField()
