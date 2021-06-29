from django.contrib import admin
from .models import Passwords, Todos


class TodosAdmin(admin.ModelAdmin):
    list_filter = ('user',)


admin.site.register(Todos, TodosAdmin)


class PasswordsAdmin(admin.ModelAdmin):
    list_filter = ('user',)


admin.site.register(Passwords, PasswordsAdmin)
