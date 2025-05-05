from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Professional)
admin.site.register(models.Clinic)
admin.site.register(models.Appointment)
admin.site.register(models.Availability)
admin.site.register(models.Patient)