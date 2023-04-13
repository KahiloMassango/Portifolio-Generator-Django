from django.contrib import admin
from .models import CustomUser, Experience, Profile, Education


admin.site.register(CustomUser)
admin.site.register(Experience)
admin.site.register(Profile)
admin.site.register(Education)
