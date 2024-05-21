from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
class BannerContactInfo(models.Model):
    address = models.CharField(max_length=255, verbose_name="Adres")
    email = models.EmailField(max_length=255, verbose_name="E-Mail")
    phone_number = models.CharField(max_length=20, verbose_name="Telefon")
    twitter_url = models.URLField(max_length=200, verbose_name="Twitter URL", blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, verbose_name="LinkedIn URL", blank=True, null=True)

    def __str__(self):
        return self.email

class Services(models.Model):
    SERVICES_CHOICES = [
        ('flaticon-money-1', 'flaticon-money-1'),
        ('flaticon-sedan-car-front', 'flaticon-sedan-car-front'),
        ('flaticon-shelter', 'flaticon-shelter'),
        ('flaticon-dollar', 'flaticon-dollar'),
        ('flaticon-trend', 'flaticon-trend'),
        ('flaticon-plumber', 'flaticon-plumber'),
        ('flaticon-building', 'flaticon-building'),
        ('flaticon-handcuff', 'flaticon-handcuff'),
    ]
    Services_Icon = models.CharField(max_length=25, choices=SERVICES_CHOICES, default='flaticon-handcuff')
    headers = models.CharField(max_length=255, verbose_name="Headers")
    Description = models.CharField(max_length=255, verbose_name="Description")
    image = models.ImageField(upload_to='services_image/')
    def __str__(self):
        return self.headers

class FooterSocialMedya(models.Model):
    SOCIAL_MEDYA_CHOICES = [
        ('icofont-twitter', 'icofont-twitter'),
        ('icofont-instagram', 'icofont-instagram'),
        ('icofont-facebook', 'icofont-facebook'),
        ('icofont-youtube', 'icofont-youtube'),
        ('icofont-linkedin', 'icofont-linkedin'),
    ]
    SocialMedya = models.CharField(max_length=30)
    SocialMedyaIcon = models.CharField(max_length=25, choices=SOCIAL_MEDYA_CHOICES)
    social_url = models.URLField(max_length=200, verbose_name="Social URL", blank=True, null=True)
    def __str__(self):
        return self.SocialMedya


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ForeignKey(Services, on_delete=models.CASCADE)
    Headers = models.CharField(max_length=200)
    date_posted = models.DateField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_image/')

    def __str__(self):
        return self.Headers