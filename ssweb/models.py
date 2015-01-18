__author__ = 'lx'
import time

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password

# Define models


# class User(models.User):
#     # id = models.Column(db.Integer, primary_key=True)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     active = models.BooleanField(default=False)


# class Shadowsocks(models.Model):
#     ss_port = models.IntegerField(unique=True)
#     ss_password = models.CharField(max_length=255)
#     ss_down_throught = models.BigIntegerField(default=0)
#     ss_up_throught = models.BigIntegerField(default=0)
#     ss_max_throught = models.BigIntegerField(default=5e9)
#     ss_active = models.BooleanField(default=True)
#     # 1:norm_user 2:nolimit_user
#     ss_user_type = models.IntegerField(default=1)
#     ss_last_get_gift_time = models.CharField(max_length=255)
#     ss_last_rest_pass_time = models.CharField(max_length=255)
#     ss_last_trans_time = models.CharField(max_length=255, default=None)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, default=None)


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