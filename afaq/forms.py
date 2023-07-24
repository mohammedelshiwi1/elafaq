from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django import forms
class question(forms.Form):
    user=forms.CharField(max_length=40)
    ques=forms.CharField(max_length=200)
 





class createuser(UserCreationForm):
    email = forms.EmailField(required=True)
    class meta:
        model=User
        fields=['username','email','password1','password2',]
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
class notifications(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    number=forms.IntegerField()
    des=forms.CharField()
