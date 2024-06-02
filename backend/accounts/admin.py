from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import User,OtpCode

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm #for adding extra form we can use adding_form field

    list_display=('email','phone_number','is_admin')
    list_filter=('is_admin',)

    # this is for form field
    fieldsets = (
        (None, {
            "fields": (
                'email','phone_number','fullname','password'
            ),
        }),
        ('Permissions',{
            "fields":(
                'is_active','is_admin','last_login'
            )
        })
    )
    
    # this is for add_form field to show fields of UserCreation Form in admin panel
    add_fieldsets=(
        (None,{
            "fields":(
                'phone_number','email','fullname','password1','password2'
            )
            }),
    )

    search_fields=('email','fullname','phone_number')
    ordering=('phone_number','fullname')

    # this is for permissions that set in User model but we did not set any permission yet,
    # so its empty but it is required to write
    filter_horizontal=()

admin.site.unregister(Group) 
admin.site.register(User,UserAdmin)
admin.site.register(OtpCode)