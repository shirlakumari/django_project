from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    #OneToOneField is same as foregin key so here user varible in this 
    #model(table) has foregin key of our current logged in user
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    #profile_pic is directory where all profile pic stored
    #and for working in python with image we have to install pillow
    # $pip install pillow
    dp = models.ImageField(default='default.jpg', upload_to='profile_pics') 

    # dunder str
    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        
        # # resizing larger image for better performance
        New_img = Image.open(self.dp.path)


        if New_img.height > 300 or New_img.width > 300:
            # 300 X 300 pixel
            output_size = (300, 300)

            New_img.thumbnail(output_size)
            New_img.save(self.dp.path)