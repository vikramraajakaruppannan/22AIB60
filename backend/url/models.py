from django.db import models
import random
import string

def generate_shortcode(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

class URL(models.Model):
    original_url = models.URLField(max_length=200)
    shortcode = models.CharField(max_length=10, unique=True, default=generate_shortcode)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)
    validity = models.PositiveIntegerField(default=30)

    def __str__(self):
        return f"{self.original_url} -> {self.shortcode}"