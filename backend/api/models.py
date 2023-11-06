from django.db import models
import random
import string


# Helper function to generate short uuid
def generate_slug():
    """Generate a unique slug with 4 characters"""
    while True:
        slug = "".join(
            random.choice(string.ascii_lowercase + string.digits) for _ in range(4)
        )
        if not Character.objects.filter(slug=slug).exists():
            return slug


class Stat(models.Model):
    physique = models.IntegerField()
    intellect = models.IntegerField()
    skill = models.IntegerField()
    perception = models.IntegerField()
    empathy = models.IntegerField()


class Character(models.Model):
    slug = models.CharField(max_length=4, unique=True, default=generate_slug, editable=False)
    title = models.CharField(max_length=50, null=True, blank=True)
    nick_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=20)
    secret_occupation = models.CharField(max_length=20, null=True, blank=True)
    faction = models.CharField(max_length=20, null=True)
    biography = models.TextField(null=True, blank=True)
    background_secret = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=20, null=True)
    portrait_filename = models.CharField(max_length=20, blank=True, null=True) 

    stats = models.OneToOneField(Stat, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.slug} {self.first_name} {self.last_name}'