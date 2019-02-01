from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(label='注册用户名',max_length=100)
    password1 = forms.CharField(label='设置密码',widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    phone_num = forms.CharField(label='电话号码',max_length=15)

