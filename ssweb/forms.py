#coding=UTF-8
__author__ = 'lx'
# from django import forms
import floppyforms as forms
from .models import MyUser, InviteCode


class UserRegisterForm(forms.Form):
    email = forms.EmailField(label=u'邮箱地址', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label=u'密码')
    confirm = forms.CharField(widget=forms.PasswordInput(), label=u'重复密码')
    invite_code = forms.CharField(label=u'邀请码', required=True)
    # accept_tos = forms.BooleanField('I accept the tos')

    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if len(password) < 7:
    #         raise forms.ValidationError("password insecure")
    #     return password

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password1 = cleaned_data['password']
        password2 = cleaned_data['confirm']
        if password1 != password2:
            raise forms.ValidationError(u"两次密码不匹配!")
        email = cleaned_data['email']
        if len(MyUser.objects.filter(email=email)) != 0:
            raise forms.ValidationError(u'邮箱地址已经被使用!')
        code = cleaned_data['invite_code']
        if len(InviteCode.objects.filter(code=code)) == 0:
            raise forms.ValidationError(u'邀请码不存在或已被使用!')
        return cleaned_data


class UserLoginForm(forms.Form):
    email = forms.EmailField(label=u'邮箱地址', required=True)
    password = forms.CharField(label=u'密码', required=True, widget=forms.PasswordInput())

    # def clean(self):
    #     cleaned_data = super(UserLoginForm, self).clean()
    #     email = cleaned_data['email']
    #     if len(MyUser.objects.filter(email=email)) == 0:
    #         raise forms.ValidationError('email not exist!')
    #     # password = cleaned_data['password']
    #     # user = MyUser.objects.get(email=email)
    #     # if user.check_password(password) is False:
    #     #     raise forms.ValidationError('password not correct!')
    #     return cleaned_data