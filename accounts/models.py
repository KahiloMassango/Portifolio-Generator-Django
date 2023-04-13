from django.db import models
import datetime
from multiselectfield import MultiSelectField
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=200)
    has_profile = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    stacks_choices = [
        ("FrontEnd Developer", "FrontEnd Developer"),
        ("BackEnd Developer", "BackEnd Developer"),
        ("Full Stack Developer", "Full Stack Developer"),
    ]
    techs_choices = (
        ("Javascript", "Javascript"),
        ("Python", "Python"),
        ("Go", "Go"),
        ("Java", "Java"),
        ("Kotlin", "Kotlin"),
        ("PHP", "PHP"),
        ("C#", "C#"),
        ("Swift", "Swift"),
        ("R", "R"),
        ("Ruby", "Ruby"),
        ("C", "C"),
        ("C++", "C++"),
        ("Matlab", "Matlab"),
        ("TypeScript", "TypeScript"),
        ("Scala", "Scala"),
        ("SQL", "SQL"),
        ("CSS", "CSS"),
        ("NoSQL", "NoSQL"),
        ("Rust", "Rust"),
        ("Perl", "Perl"),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=500, default='', blank=True)
    user_url = models.SlugField(max_length=300)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/%Y/%m/%d')  # noqa
    country = CountryField()
    stack = models.CharField(choices=stacks_choices, default="FR", max_length=200)  # noqa
    company = models.CharField(max_length=200, default='default', blank=True,)
    company_l = models.URLField(max_length=200, default='default.com', blank=True)  # noqa
    github = models.CharField(max_length=200, default='default')
    github_l = models.URLField(max_length=200, default='default.com', blank=True)  # noqa
    linkedin = models.CharField(max_length=200, default='default')
    linkedin_l = models.URLField(max_length=200, default='default.com', blank=True)  # noqa
    twitter = models.CharField(max_length=200, default='default', blank=True)
    twitter_l = models.URLField(max_length=200, default='default.com', blank=True)  # noqa
    webpage = models.URLField(max_length=200, blank=True, null=True)
    techs = MultiSelectField(choices=techs_choices, max_length=200)

    def __str__(self):
        return f'{self.user.username}'


class Experience(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(1999, datetime.date.today().year+1)]
    YEAR_CHOICES2 = [(f"{i}", f"{i}") for i in range(1999, datetime.date.today().year+1)]  # noqa
    YEAR_CHOICES2.append(("current", "current"))

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, blank=False, null=False)
    start = models.IntegerField(choices=YEAR_CHOICES)
    end = models.CharField(choices=YEAR_CHOICES2, max_length=10)
    work = models.CharField(max_length=254, blank=False, null=False)

    def __str__(self):
        return self.work


class Education(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(1999, datetime.date.today().year+1)]
    YEAR_CHOICES2 = [(f"{i}", f"{i}") for i in range(1999, datetime.date.today().year+1)]  # noqa
    YEAR_CHOICES2.append(("current", "current"))

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=100, blank=False)
    start = models.IntegerField(choices=YEAR_CHOICES)
    end = models.CharField(choices=YEAR_CHOICES2, max_length=10)
    title = models.CharField(max_length=254)

    def __str__(self):
        return self.title
