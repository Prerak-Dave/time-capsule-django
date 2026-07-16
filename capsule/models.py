from django.db import models
from django.contrib.auth import get_user_model

class Capsule(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=250)
    unlock_date = models.DateField()
    sender = models.OneToOneField(get_user_model())
    receiver = models.ForeignKey(get_user_model(), related_name="receivers")

    def __str__(self):
        return self.title

class ImgCapsule(models.Model):
    memory = models.ForeignKey(Capsule, on_delete = models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"image for {self.memory}"
