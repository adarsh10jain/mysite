from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_id=models.AutoField
    name=models.CharField(max_length=25)
    phone=models.CharField(max_length=10)
    subject=models.CharField(max_length=50)
    desc=models.TextField(max_length=200)
    email=models.EmailField()

    def __str__(self):
        return self.name +"-"+self.email


class Project(models.Model):
    project_id=models.AutoField
    name=models.CharField(max_length=50)
    desc=models.TextField()
    image=models.ImageField()
    exe=models.FileField(blank=True)
    tech_used=models.TextField()
    thumbnail_img=models.ImageField()
    image2=models.ImageField(blank=True)
    image3=models.ImageField(blank=True)
    image4=models.ImageField(blank=True)
    image5=models.ImageField(blank=True)


    def __str__(self):
        return self.name



class Personal_info(models.Model):
    resume=models.FileField()
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name