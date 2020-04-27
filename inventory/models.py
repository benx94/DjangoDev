from django.db import models

class Test(models.Model):
    machine = models.CharField(max_length=200, unique=True)
    login = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)



    class Meta:
        verbose_name = 'inventaire'

    def __str__(self):
        return self.machine

class Materiel(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'matériel'

    def __str__(self):
        return self.name


class Owner(models.Model):
    login = models.CharField(max_length=200, unique=True)
    materiel = models.OneToOneField(Materiel, on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = 'propriétaire'

    def __str__(self):
        return self.login
