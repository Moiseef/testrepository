from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product
from .models import Image
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, CheckboxSelectMultiple, ClearableFileInput, CheckboxInput
from django.forms import inlineformset_factory
from .models import Contact

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user                
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "full_text",
            "price",
            "date",
            "facilities",
            "rooms",
            "bath_rooms",
            "email",
            "phone",
            "address",
            "skype",
            "instagram",
            "whatsapp"
        ]
        widgets = {
            "title": TextInput(attrs={
            'class': 'form-control mt-1 mb-1',
            'placeholder': 'Tltle',
            'type': 'text'
            }),
            "full_text": Textarea(attrs={
            'class': 'form-control mt-1 mb-1',
            'placeholder': 'Description',
            'type': 'text'
            }),
            "price": TextInput(attrs={
            'type': 'number',
            'min': '0.00', 
            'max': '999000.00', 
            'step': '0.01', 
            'name': 'price'           
            }),
             "rooms": TextInput(attrs={
            'type': 'number',
            'label': 'rooms',
            'min': '0', 
            'max': '10', 
            'step': '1', 
            'name': 'rooms'           
            }),
            "bath_rooms": TextInput(attrs={
            'type': 'number',
            'label': 'bath rooms',
            'min': '0', 
            'max': '10', 
            'step': '1',
            'name': 'bath_rooms'             
            }),
            "facilities": CheckboxSelectMultiple(attrs={
            'type': 'checkbox',         
            }),
            "date": DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control mt-1 mb-1',
            'name': 'Date'
            }),
            "email": TextInput(attrs={
            'type': 'email',
            'class': 'form-control mt-1 mb-1',
            'name': 'email'
            }),
            "phone": TextInput(attrs={
            'type': 'tel',
            'class': 'form-control mt-1 mb-1',
            'name': 'phone'
            }),
            "address": TextInput(attrs={
            'type': 'text',
            'class': 'form-control mt-1 mb-1',
            'name': 'address'
            }),
            "skype": TextInput(attrs={
            'type': 'text',
            'class': 'form-control mt-1 mb-1',
            'name': 'skype',
            'required': 'false'
            }),
            "instagram": TextInput(attrs={
            'type': 'text',
            'class': 'form-control mt-1 mb-1',
            'name': 'instagram',
            'required': 'false'
            }),
            "whatsapp": TextInput(attrs={
            'type': 'text',
            'class': 'form-control mt-1 mb-1',
            'name': 'whatsapp',
            'required': 'false'
            }),

        }


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple": True, 'class': 'form-control mt-1 mb-5', 'name': 'Images',}),
    )

    class Meta:
        model = Image
        fields = ("image",)


class ContactForm(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contact
        # Поля, которые будем использовать для заполнения
        fields = ['first_name', 'phone', 'email', 'message']
        widgets = {
            'message': Textarea(
                attrs={
            'class': 'form-control',
            'placeholder': 'Write your message here',
            'name': 'message',
            'type': 'text'
            }),
            "phone": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone',
            'name': 'phone',
            'type': 'tel'
            }),
            "first_name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name',
            'name': 'name',
            'type': 'text'
            }),
            "email": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'name': 'email',
            'type': 'email'
            }),
        }

