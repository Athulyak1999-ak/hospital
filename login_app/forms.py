from django import forms
# from .models import UserProfile, LoginTable
# from django.contrib.auth.models import User
from admins.models import Patient, LoginTable


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['username', 'address', 'phone_number', 'password', 'con_password']


class LoginTableForm(forms.ModelForm):
    class Meta:
        model = LoginTable
        fields = ['username', 'password', 'password2']

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['username', 'password', 'password2']
#
# class LoginTableForm(forms.ModelForm):
#     username = forms.CharField(max_length=30)
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = LoginTable
#         fields = ['username', 'password', 'password2']
#
#     def save(self, commit=True):
#         user = User.objects.create_user(
#             username=self.cleaned_data['username'],
#             password=self.cleaned_data['password'],
#         )
#         login_table = super().save(commit=False)
#         login_table.username = user  # Link the user to the LoginTable instance
#         if commit:
#             login_table.save()
#         return login_table
