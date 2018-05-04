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
    severity = models.FloatField()
    timestamp = models.DateTimeField()
    force_1 = models.IntegerField(default=0)
    force_2 = models.IntegerField(default=0)
    force_3 = models.IntegerField(default=0)
    force_4 = models.IntegerField(default=0)
    force_5 = models.IntegerField(default=0)
    force_6 = models.IntegerField(default=0)
    force_7 = models.IntegerField(default=0)
    force_8 = models.IntegerField(default=0)
    force_9 = models.IntegerField(default=0)
    force_10 = models.IntegerField(default=0)
    force_11 = models.IntegerField(default=0)
    force_12 = models.IntegerField(default=0)
    axis_1 = models.IntegerField(default=0)
    axis_3_x = models.IntegerField(default=0)
    axis_3_y = models.IntegerField(default=0)
    axis_3_z = models.IntegerField(default=0)
