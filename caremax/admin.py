from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(Test)
admin.site.register(Treatment)
admin.site.register(Bill)
admin.site.register(Stockcategory)
admin.site.register(Stock)

