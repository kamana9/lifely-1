from django.contrib import admin
from .models import Passwords, Todos, Events


class TodosAdmin(admin.ModelAdmin):
    list_filter = ('user',)


admin.site.register(Todos, TodosAdmin)


class PasswordsAdmin(admin.ModelAdmin):
    list_filter = ('user',)


admin.site.register(Events, PasswordsAdmin)


class PasswordsAdmin(admin.ModelAdmin):
    list_filter = ('user',)


admin.site.register(Passwords, PasswordsAdmin)
