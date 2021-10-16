from django.db import models

from authentication.models import User


class PublicProfile(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    photo = models.ImageField(
        default="", upload_to='store_image/', null=True, blank=True)
    fullname = models.CharField(
        default=str(User.username), max_length=255, blank=False, null=False)
    shortBio = models.CharField(max_length=555, blank=True, null=True)
    PRONOUNS = (
        ("ey/em", "ey/em"),
        ("he/him", "he/him"),
        ("ne/nem", "ne/nem"),
        ("she/her", "she/her"),
        ("they/them", "they/them"),
        ("ve/ver", "ve/ver"),
        ("xe/xem", "xe/xem"),
        ("xie/xem", "xie/xem"),
        ("ze/zir", "ze/zir"),
    )
    pronouns = models.CharField(
        choices=PRONOUNS, max_length=20, blank=True, null=True, help_text="Add your Pronouns")
    website = models.URLField(
        blank=True, help_text="Add a link to drive traffic to your site")
    username = models.CharField(
        default=str(User.username), max_length=255, blank=False, null=False)
    age = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(default=str(User.username), max_length=255)

    def __str__(self):
        return self.fullname


class AccountSettings(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    email = models.EmailField(default=str(
        User.username), blank=False, null=False)
    password = models.CharField(max_length=255, blank=True, null=True)
    COUNTRY = (
        ("Iran", "Iran"),
        ("America", "America"),
        ("England", "England"),
        ("France", "France"),
        ("Italy", "Italy"),
    )
    country = models.CharField(
        choices=COUNTRY, max_length=68, blank=False, null=False)
    LANGUAGE = (
        ("Persian", "Persian"),
        ("English(US)", "English(US)"),
        ("English(UK)", "English(UK)"),
        ("French", "French"),
        ("Italiano", "Italiano"),
    )
    language = models.CharField(
        choices=LANGUAGE, max_length=68, blank=False, null=False)
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Non_Binary", "Non_Binary"),
    )
    gender = models.CharField(
        choices=GENDER, max_length=24, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(default=str(User.username), max_length=255)

    def __str__(self):
        return self.email
