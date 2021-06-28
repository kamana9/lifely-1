from django.contrib import admin

# Register your models here.
from .models import Aboutus, FeedBacks


admin.site.register(Aboutus)


class FeedBacksAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    list_filter = ('email',)


admin.site.register(FeedBacks, FeedBacksAdmin)
