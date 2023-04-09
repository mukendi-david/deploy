from django.contrib.admin import AdminSite
from users.admin import *
from users.models import OtpCode
from verify.models import *

class CustomAdminSite(AdminSite):
    site_header = 'Custom administration'
    site_title = 'Custom site admin'

    def __init__(self, name='admin'):
        super().__init__(name)

    def has_permission(self, request):
        return request.user.is_superuser


admin_site = CustomAdminSite()

admin_site.register(CustomUser, CustomUserAdmin)
admin_site.register(OtpCode)
admin_site.register(Course)
admin_site.register(Cotes)
admin_site.register(Student)
