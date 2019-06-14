from django.contrib import admin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('username', 'email','first_name','last_name','phone')
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email','username', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','phone','housenumber','locality','village','mandal','district','pincode')}),

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('username','email','first_name','last_name','phone')
    ordering = ('username','email','phone')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
