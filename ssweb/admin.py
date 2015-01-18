from django.contrib import admin

from ssweb.models import MyUser

# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'ss_port',
                    'ss_password', 'ss_down_throught',
                    'ss_up_throught', 'ss_max_throught',
                    'ss_active', 'ss_user_type', 'ss_last_get_gift_time',
                    'ss_last_rest_pass_time', 'ss_last_trans_time')


admin.site.register(MyUser, MyUserAdmin)
