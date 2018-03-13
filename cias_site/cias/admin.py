from django.contrib import admin

from .models import *

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(MedicalStaff)
admin.site.register(ImpactEvent)
