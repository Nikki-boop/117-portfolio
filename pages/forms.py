from django import forms

class ContactForm(forms.Form):

    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=100, required=False)