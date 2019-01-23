from django.db import models


class Member(models.Model):
    name = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.email
