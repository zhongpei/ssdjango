__author__ = 'lx'

from django.db import models
from django.contrib.auth.models import AbstractUser


# Define models

class MyUser(AbstractUser):
    ss_port = models.IntegerField(unique=True, default=9630)
    ss_password = models.CharField(max_length=255)
    ss_down_throught = models.BigIntegerField(default=0)
    ss_up_throught = models.BigIntegerField(default=0)
    ss_max_throught = models.BigIntegerField(default=5e9)
    ss_active = models.BooleanField(default=True)
    # 1:norm_user 2:nolimit_user
    ss_user_type = models.IntegerField(default=1)
    ss_last_get_gift_time = models.CharField(max_length=255)
    ss_last_rest_pass_time = models.CharField(max_length=255)
    ss_last_trans_time = models.CharField(max_length=255)


class InviteCode(models.Model):
    code = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.code