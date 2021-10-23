from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    contact = models.CharField(max_length=150)
    image = models.ImageField(default='Default.jpg', upload_to='profile_pics')

    class Meta:
        db_table = 'users_profile'

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
