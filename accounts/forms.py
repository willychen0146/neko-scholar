from django.forms import ModelForm, FileField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class AccountForm(ModelForm):
	class Meta:
		model = Account
		fields = '__all__'
		exclude = ['user']

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = '__all__'

class ImageUploadForm(ModelForm):
    image = FileField(label='Upload Image', help_text='Only image files are allowed.', widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = Post
        fields = ['image']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class EmailForm(forms.Form):
    recipient_email = forms.EmailField(label='Recipient Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=Account.objects.none(), required=True)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MessageForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['receiver'].queryset = Account.objects.exclude(user=user)

    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']