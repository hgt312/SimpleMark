# -*- coding:utf-8 -*-

import re

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    mobile = forms.CharField(required=True)
    password_1 = forms.CharField(required=True, min_length=6)
    password_2 = forms.CharField(required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        regex_username = r'^[a-zA-Z][a-zA-Z0-9_-]{2,14}[a-zA-Z0-9]$'
        p = re.compile(regex_username)
        if p.match(username):
            return username
        else:
            raise forms.ValidationError('用户名非法', code="username_invalid")

