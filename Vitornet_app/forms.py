from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        user= User.objects.filter(username=username).first()
        if user:
             raise forms.ValidationError('Nome de usuario já cadastrado')

        if '@' in username or '#' in username or ' ' in username:
            raise forms.ValidationError('Nome de usuario com caracteres invalidos')
       
        if not username:
            raise forms.ValidationError('Nome de usuario deve ser preenchido')
        
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not password:
            raise forms.ValidationError('Senha não pode estar vazia')
        return password
    def clean_email(self):
        email = self.cleaned_data.get('email')


        email_filter= User.objects.filter(email=email).first()
        if email_filter:
             raise forms.ValidationError('Email já cadastrado')

        if '@' not in email or '.com' not in email:
            raise forms.ValidationError('Digite um email válido')
        if not email:
            raise forms.ValidationError('Email não pode estar vazio')
        return email
    def clean_first_name(self):
         first_name = self.cleaned_data.get('first_name')
        
         if not first_name:
            raise forms.ValidationError("Primeiro nome não pode estar vazio")
                
         return first_name
    def clean_last_name(self):
         last_name = self.cleaned_data.get('last_name')
        
         if not last_name:
            raise forms.ValidationError("Ultimo nome não pode estar vazio")
                
         return last_name