from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    birth = models.DateField()
    email = models.EmailField()



    def __str__(self):
        return f'[{self.pk}] {self.name}'


    def get_absolute_url(self):
        return f'/member/{self.pk}/'