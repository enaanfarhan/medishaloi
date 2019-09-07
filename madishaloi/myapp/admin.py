from django.contrib import admin

# Register your models here.

from .models import Doctor,Medicine,Ambulance,author

admin.site.register(Doctor)
admin.site.register(Medicine)
admin.site.register(Ambulance)
admin.site.register(author)

