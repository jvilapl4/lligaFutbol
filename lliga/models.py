from django.db import models

# Create your models here.

class Lliga(models.Model):
    nom = models.CharField(max_length=100)
    temporada = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nom} - {self.temporada}"

class Equip(models.Model):
    nom = models.CharField(max_length=100)
    ciutat = models.CharField(max_length=100)
    lliga = models.ForeignKey(Lliga, related_name='equips', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Jugador(models.Model):
    nom = models.CharField(max_length=100)
    edat = models.IntegerField()
    posicio = models.CharField(max_length=50)
    equip = models.ForeignKey(Equip, related_name='jugadors', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Partit(models.Model):
    lliga = models.ForeignKey(Lliga, related_name='partits', on_delete=models.CASCADE)
    equip_local = models.ForeignKey(Equip, related_name='partits_local', on_delete=models.CASCADE)
    equip_visitant = models.ForeignKey(Equip, related_name='partits_visitant', on_delete=models.CASCADE)
    data_partit = models.DateTimeField()
    gols_local = models.IntegerField(default=0)
    gols_visitant = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.equip_local} vs {self.equip_visitant} - {self.data_partit.strftime('%Y-%m-%d %H:%M')}"

