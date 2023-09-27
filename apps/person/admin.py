from django.contrib import admin

from .models import Pendidikan, PengalamanKerja, Person

# Register your models here.
admin.site.register(Pendidikan)
admin.site.register(PengalamanKerja)
admin.site.register(Person)
