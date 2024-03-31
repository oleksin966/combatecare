from django import forms
from .models import CustomUser, UserProfile
from django.forms.widgets import ClearableFileInput

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Введіть логін'
        }),
        label='Позивний(username)'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Введіть пароль'
        }),
        label='Пароль'
    )

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='Ім\'я користувача')
    first_name = forms.CharField(label='Ім\'я', required=False)
    last_name = forms.CharField(label='Прізвище', required=False)
    info = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), label='Інформація', label_suffix='', required=False)
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Телефон', required=False)
    avatar = forms.ImageField(label='Фото профілю', required=False, help_text='Завантажте фото профілю. Формати JPG та PNG підтримуються.',)

    STATUS_CHOICES = [
        ('IN_TRANSIT', 'В дорозі'),
        ('FREE', 'Вільний'),
        ('UNAVAILABLE', 'Недоступний'),
    ]

    military_military_unit = forms.CharField(label='Військовий підрозділ', required=False)
    military_military_rank = forms.CharField(label='Військове звання', required=False)
    deliveryman_status = forms.ChoiceField(choices=STATUS_CHOICES, label='Статус', 
        required=False,  widget=forms.Select(attrs={'style': 'height: 30px;'}),)

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'info', 'avatar', 
            'military_military_unit', 'military_military_rank', 
            'deliveryman_status')

    def clean(self):
        cleaned_data = super().clean()
        for field_name, field_value in cleaned_data.items():
            if field_value is None:
                cleaned_data[field_name] = '-'
        return cleaned_data

class MilitaryRegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter Username'
        }),
        label='Позивний(username)'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter Password'
        }),
        label='Пароль'
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Введіть Ім\'я'
        }),
        label='Ім\'я',
        required=False
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Введіть Прізвище'
        }),
        label='Прізвище',
        required=False
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Введіть e-mail'
        }),
        label='e-mail',
        required=False
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Номер Телефону'
        }),
        label='Номер телефону',
        required=False
    )

    military_unit = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Введіть № В/Ч'
        }),
        label='Військова частина',
        required=False
    )
    military_rank = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Введіть військове звання'
        }),
        label='Віськове звання',
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        for field_name, field_value in cleaned_data.items():
            if field_value is None:
                cleaned_data[field_name] = '-'
        return cleaned_data