from django.db import models

# Create your models here.

class Categories(models.Model):
    nom = models.CharField(max_length=255)
    id = models.IntegerField(unique=True, primary_key=True)

    def __str__(self):
        return self.nom

class Livre(models.Model):
    isbn = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    linodate = models.CharField(max_length=100)
    editions = models.CharField(max_length=255)
    exemplaire = models.IntegerField()
    categoried = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Consultes(models.Model):
    date = models.DateField()
    livred = models.ForeignKey(Livre, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

class Theses(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Telecharge(models.Model):
    dates = models.DateField()
    thesed = models.ForeignKey(Theses, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.dates)
