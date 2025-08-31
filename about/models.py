from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    # Return a string (the title in this case)
    def __str__(self):
        return self.title