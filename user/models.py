from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
# from django.contrib.auth.models import AbstractUser
#
#
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genreChoice = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Children', 'Children'),
        ('Comedy', 'Comedy'),
        ('Crime', 'Crime'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Film-Noir', 'Film-Noir'),
        ('Horror', 'Horror'),
        ('Musical', 'Musical'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),
        ('War', 'War'),
        ('Western', 'Western'),
    )
    genderChoice = (
        ('F', 'F'),
        ('M', 'M'),
        ('N/A', 'N/A'),
    )
    # *1: "Under 18"
    # *18: "18-24"
    # *25: "25-34"
    # *35: "35-44"
    # *45: "45-49"
    # *50: "50-55"
    # *56: "56+"

    # 后面是网页显示的
    ageChoice = (
        ('1', 'Under 18'),
        ('18', '18-24'),
        ('25', '25-34'),
        ('35', '35-44'),
        ('45', '45-49'),
        ('50', '50-55'),
        ('56', '56+'),
    )

    occupationChoice = (
        ('0:', 'other'),
        ('1:', 'academic/educator'),
        ('2:', 'artist'),
        ('3:', 'clerical/admin'),
        ('4:', 'N'),
        ('5:', 'N'),
        ('6:', 'N'),
        ('7:', 'N'),
        ('8:', 'N'),
        ('9:', 'N'),
        ('10', 'N'),
        ('11', 'N'),
        ('12', 'N'),
        ('13', 'N'),
        ('14', 'N'),
        ('15', 'N'),
        ('16', 'N'),
        ('17', 'N'),
        ('18', 'N'),
        ('19', 'N'),
        ('20', 'N')
    )

    # UserID::Gender::Age::Occupation::Zip - code

    # *0: "other" or not specified
    # *1: "academic/educator"
    # *2: "artist"
    # *3: "clerical/admin"
    # *4: "college/grad student"
    # *5: "customer service"
    # *6: "doctor/health care"
    # *7: "executive/managerial"
    # *8: "farmer"
    # *9: "homemaker"
    # *10: "K-12 student"
    # *11: "lawyer"
    # *12: "programmer"
    # *13: "retired"
    # *14: "sales/marketing"
    # *15: "scientist"
    # *16: "self-employed"
    # *17: "technician/engineer"
    # *18: "tradesman/craftsman"
    # *19: "unemployed"
    # *20: "writer"

    # UserID = models.IntegerField(blank=True, default=0)
    gender = models.CharField(max_length=100, default='', choices=genderChoice)
    age = models.CharField(max_length=4, default='', choices=ageChoice)
    occupation = models.CharField(max_length=100, default='')


    def create_user_profile(sender, instance, created, **kwargs):
        if created:
             Profile.objects.get_or_create(user=instance)

    post_save.connect(create_user_profile, sender=User)
