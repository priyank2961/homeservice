from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomerRegModel)
admin.site.register(EmployeeRegModel)
admin.site.register(Appointment)
admin.site.register(pendingAppointment)
