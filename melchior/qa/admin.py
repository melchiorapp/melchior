from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm

from qa.models import GenericUser, InternalUser, Organization

# Register your models here.
class GenericUserAdmin(UserAdmin):
  change_user_password_template = None
  fieldsets = (
    (None, {'fields':('email', 'password', 'first_name', 'last_name', 'is_admin', 'is_active', 'phone_number', 'organization')}),
  )
  add_fieldsets=(
    (None,{
      'fields':('email', 'password')
    })
  )
  form= UserChangeForm
  add_form= UserCreationForm
  change_password_form = AdminPasswordChangeForm

  # password_change_url = urlresolvers.reverse('admin:auth_user_password_change', args=(1,))

  list_display= ('email', 'first_name', 'last_name', 'is_admin', 'phone_number')
  list_filter= ('email', 'first_name', 'last_name', 'is_admin', 'phone_number')
  search_fields= ('email', 'first_name', 'last_name')
  filter_horizontal= ()
  ordering= ('email',)

  model= GenericUser
  
  

# admin.site.unregister(GenericUser)
admin.site.register(GenericUser, GenericUserAdmin)
admin.site.register(InternalUser)
admin.site.register(Organization)

admin.autodiscover()