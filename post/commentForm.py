from . import models
from django import forms
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
           # self.fields[field].widget.attrs.update({'class': 'form-control fh5co_footer_text_box','type':'text','placeholder':'متن خود را برای ما ارسال کنید...','aria-describedby':'basic-addon1','style':'border: 1px solid #00989B'})
            self.fields[field].widget=forms.TextInput(attrs={'class': 'form-control fh5co_footer_text_box','type':'text','placeholder':'متن خود را برای ما ارسال کنید...','aria-describedby':'basic-addon1','style':'border: 1px ;solid #00989B;'})
    class Meta:
        model = models.comment
        fields = ['text']