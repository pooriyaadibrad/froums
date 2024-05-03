from django import forms
from . import models
class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            if field == 'email':
                self.fields[field].widget.attrs.update({'placeholder': 'Email'})
            if field == 'password':
                self.fields[field].widget.attrs.update({'placeholder': 'Password','type':'password','name':'password'})
                self.fields[field].widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'})

    class Meta:
        model = models.user
        fields = ('email', 'password',)

        #password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))