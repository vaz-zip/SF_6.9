from django.db import models
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    picture = models.FileField(upload_to='images/')

    def __str__(self):
        return self.name


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        new_person = Person.objects.create(user=user, name=user.username, picture='images/default.png')
        new_person.save()
        return user
