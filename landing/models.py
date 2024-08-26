from django.db import models

# Create your models here.
class User(models.Model):
    # fidc = models.UUIDField(default=uuid.uuid4().int, unique=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email= models.EmailField(max_length = 254, unique=True, default="example@gmail.com")
    password = models.CharField(max_length=50, blank=True, null=True)
    institution = models.CharField(max_length=200, blank=True, null=True)
    subjects = models.CharField(max_length=300, default="physics,math,chemistry")
    quizes=  models.JSONField(default=dict)
    @property
    def subjectlist(self):
        l = self.subjects.split(",")
        return l

