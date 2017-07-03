from django.contrib import admin

from .models import Properties
from .models import Demands

admin.site.register(Properties)
admin.site.register(Demands)