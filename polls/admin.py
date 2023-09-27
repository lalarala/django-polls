from django.contrib import admin

from .models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)

LOGIN_REDIRECT_URL = '/admin'
LOGOUT_REDIRECT_URL = '/admin'