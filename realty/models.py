from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from phone_field import PhoneField
from django.contrib.auth.models import User


# Create your models here.


class Home_articl(models.Model):
    title = models.CharField('Title', max_length=50)
    mutetext = models.CharField('Mute', max_length=50)
    full_text = models.TextField('Articl')
    venue_image = models.ImageField(
        'Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home title'
        verbose_name_plural = 'Home titles'


class Home_slide(models.Model):
    title = models.CharField('Title', max_length=50)
    text_slide = models.CharField('Text', max_length=250)
    link_text = models.CharField('Button', default='Link', max_length=50)
    link_slide = models.CharField('Link', max_length=50)
    slide_image = models.ImageField(
        'Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home slide'
        verbose_name = 'Home slides'


class Logo(models.Model):
    title = models.CharField('Title', max_length=50, default='logo')
    logo_image = models.ImageField(
        'Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'


class About_articl(models.Model):
    title = models.CharField('Title', max_length=50)
    mutetext = models.CharField('Mute', max_length=50)
    full_text = models.TextField('Articl')
    venue_image = models.ImageField(
        'Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About aricl'
        verbose_name_plural = 'About articles'


class About_slide(models.Model):
    title = models.CharField('Title', max_length=50)
    text_slide = models.CharField('Text', max_length=250)
    link_text = models.CharField('Button', default='Link', max_length=50)
    link_slide = models.CharField('Link', max_length=50)
    slide_image = models.ImageField(
        'Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About slide'
        verbose_name_plural = 'About slides'


class Title_contact(models.Model):
    title = models.CharField('Title', max_length=50)
    full_text = models.TextField('Articl')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Contact title'
        verbose_name_plural = 'Contact titles'


class Call_us(models.Model):
    title = models.CharField('Title', max_length=50)
    text = models.CharField('Text', max_length=250)
    phone_first = models.CharField('mobile', max_length=50)
    phone_second = models.CharField('phone', max_length=50)
    link_fph = models.CharField('Link_mobile', default='#', max_length=50)
    link_sph = models.CharField('Link_phone', default='#', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Call us block'
        verbose_name_plural = 'Call us blocks'


class Email_us(models.Model):
    title = models.CharField('Title', max_length=50)
    text = models.CharField('Text', max_length=250)
    link_mail = models.CharField('Link_mail', default='#', max_length=50)
    email_name = models.CharField('email_name', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Email us block'
        verbose_name_plural = 'Email us blocks'


class Social_us(models.Model):
    title = models.CharField('Title', max_length=50)
    text = models.CharField('Text', max_length=250)
    link_face = models.CharField('Link_face', default='#', max_length=50)
    link_inst = models.CharField('Link_inst', default='#', max_length=50)
    link_twit = models.CharField('Link_twit', default='#', max_length=50)
    link_in = models.CharField('Link_in', default='#', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Social us block'
        verbose_name_plural = 'Social us blocks'


class Contact_form(models.Model):
    title = models.CharField('Title', default='Send us message', max_length=50)
    label_name = models.CharField('Title', default='Your name', max_length=50)
    label_email = models.CharField(
        'Title', default='Email address', max_length=50)
    label_mobile = models.CharField(
        'Title', default='Mobile number', max_length=50)
    label_message = models.CharField(
        'Title', default='Message ', max_length=50)
    info = models.CharField(
        'Text', default='By submitting this form you agree to our terms and conditions.', max_length=250)
    label_btn = models.CharField('Title', default='Send', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Contact form'
        verbose_name_plural = 'Contact forms'

MY_CHOICES = (('item_key1', 'Elevator'),
              ('item_key2', 'Air conditioner'),
              ('item_key3', 'Garage'),
              ('item_key4', 'Pool'),)

class Product(models.Model):
    title = models.CharField(max_length=150)
    full_text = models.TextField('Articl', max_length=1000, default='full text')
    rooms = models.IntegerField('Room', default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    bath_rooms = models.IntegerField('Bath room', default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    price = models.DecimalField('Price', max_digits=10, decimal_places=2, default='1')
    facilities = MultiSelectField(choices=MY_CHOICES, max_choices=4, max_length=50, default=None)
    label_btn = models.CharField('Button', default='Add to Wishlist', max_length=50)
    date = models.DateTimeField('Publication date', null=True, blank=True)
    email = models.EmailField(max_length = 254, default=None)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address = models.CharField('Address', max_length=350, default='12345 Moscow, Arbat 1')
    skype = models.URLField(max_length = 200, default=None, blank=True)
    instagram = models.URLField(max_length = 200, default=None, blank=True)
    whatsapp = models.URLField(max_length = 200, default=None, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/realty/{self.id}'



class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', blank=True)
    image = models.ImageField('Image', blank=True, upload_to="images/")

    def __str__(self):
        return self.product.title 

# Contact forms
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=1000)
    

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email
