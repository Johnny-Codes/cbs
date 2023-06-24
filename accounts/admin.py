from django.contrib import admin
from accounts.models import User, Business

# Register your models here.

admin.site.register(Business)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
    )
