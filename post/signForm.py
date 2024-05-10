from django import forms
from . import models
class SignForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field== 'password':
                self.fields[field].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
            self.fields[field].widget.attrs = {'class': 'form-control'}

    repassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Re-password'}))
    class Meta:
        model=models.user
        fields=('name','family','studentCode','email','password')