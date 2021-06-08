from django.contrib import admin
from .models import Contact,Blogpost,Client
# Register your models here.
admin.site.register(Contact)

admin.site.register(Blogpost)
admin.site.register(Client)