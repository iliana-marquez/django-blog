from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)

    # Return a string (the title in this case)
    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    # return a string
    def __str__(self):
        return f"Collaboration request from {self.name}"