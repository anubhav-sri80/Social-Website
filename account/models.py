from django.db import models
from django.conf import settings

from PIL import Image
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth= models.DateField(blank=True,null=True)
    photo= models.ImageField(default='default.jpg',upload_to='profile_pics',
                            )

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
    