from django.contrib import admin
from .models import Question,UserResponse

admin.site.register(Question)
admin.site.register(UserResponse)