from django.contrib import admin

from .models import Materiel
from .models import Owner
from .models import Test

admin.site.register(Materiel)
admin.site.register(Owner)
admin.site.register(Test)