from django.contrib import admin

from users.models import CustomUser


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


# admin.site.unregister(User)
admin.site.register(CustomUser, UserAdmin)
