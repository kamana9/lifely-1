from django.contrib import admin
from .models import Passwords


class PasswordsAdmin(admin.ModelAdmin):
    list_filter = ('user',)


admin.site.register(Passwords, PasswordsAdmin)
