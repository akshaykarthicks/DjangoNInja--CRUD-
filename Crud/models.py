from django.db import models
from django.core.validators import MinLengthValidator

class Item(models.Model):
    name = models.CharField(
        max_length=50, 
        validators=[MinLengthValidator(3)]
    )
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

from django.contrib.auth.models import User
import secrets
#authntication token model !!
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, primary_key=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)


    def generate_key(self):
        return secrets.token_hex(20)

    def __str__(self):
        return self.key