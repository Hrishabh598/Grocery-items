from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_message(self):
        em = self.cleaned_data.get("email")
        dbuser = User.objects.filter(email=em)

        if not dbuser:
            return "not in db"
        return em;