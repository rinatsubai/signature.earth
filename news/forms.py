from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    subject = forms.CharField(label = 'Topic', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label = 'Your email text', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField()
    
class UserLoginForm (AuthenticationForm):
    username = forms.CharField(label = 'User Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = 'User Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label = 'Strong Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label = 'Verify Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        # exclude = ()
        fields = ['title', 'content', 'email', 'category', 'brand', 'facebook', 'telegram', 'twitter', 'youtube', 'photoUrl']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Арсений Катков'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEO'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ceo@rep.earth'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://facebook.com/...'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://t.me/...'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://twitter.com/...'}),
            'youtube': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://youtube.com/channel/...'}),
            'photo': forms.FileField(label='Select a file', help_text='max. 42 mb'),
            'photoUrl': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://reputation.moscow/wp-content/uploads/...'})
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Name should not start from the Number')
        return title


# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.ImageField()



    
# class SearchForm(forms.ModelForm):
#     class Meta:
#         # model = News
#         fields = ['search']
#         widgets = {
#             'search': forms.TextInput
#             (attrs={'class': 'form-control'}),
#         }

    # def clean_search(self):
    #     search = self.cleaned_data['search']
    #     return search