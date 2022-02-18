from django.db import models

class Yonalish(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Student(models.Model):
    yonalish =models.ForeignKey(Yonalish,on_delete=models.PROTECT)
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to="Rasmlar/")

    def __str__(self):
        return self.ism

        