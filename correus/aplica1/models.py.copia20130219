# Create your models here.
#encoding:utf-8

from django.db import models

class Tipus_Organismes(models.Model):
    nom = models.TextField(max_length="30")

    def __unicode__(self):
        return self.nom

    class Meta:
        ordering = ["nom"]


class Organismes(models.Model):
    codi = models.CharField(max_length=6, primary_key=True)
    organisme = models.ForeignKey(Tipus_Organismes)
    nom = models.CharField(max_length=30)
    adreca = models.CharField(max_length=50)
    poblacio = models.CharField(max_length=30)
    cp = models.CharField(max_length=5)
    email1 = models.EmailField()
    web = models.URLField(blank=True)
    tel1 = models.CharField(max_length=9)
    fax1 = models.CharField(max_length=9, blank=True)
    notes = models.TextField(help_text="Escriu una nota ", verbose_name="Notes", blank=True)

    def __unicode__(self):
        return self.nom

    class Meta:
        ordering = ["nom"]

class Carrecs(models.Model):
    nom = models.TextField(max_length="30")

    def __unicode__(self):
        return self.nom

    class Meta:
        ordering = ["nom"]

class Usuaris(models.Model):
    nom = models.CharField(max_length=30)
    cognoms = models.CharField(max_length=50)
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True)
    tel1 = models.CharField(max_length=9, blank=True)
    imagen = models.ImageField(upload_to='fotos', verbose_name='Foto', blank=True)
    notes = models.TextField(help_text="Escriu una nota ", verbose_name="Notes", blank=True)
    carrec = models.ForeignKey(Carrecs)
    organisme = models.ForeignKey(Organismes)

    def __unicode__(self):
        return u'%s %s  |   %s  |  %s %s' %(self.cognoms,self.nom,self.carrec, self.organisme.organisme, self.organisme)

    class Meta:
        ordering = ["organisme","cognoms"]


class Projectes(models.Model):
    nom = models.TextField(max_length="30")
    descripcio = models.TextField(max_length="100")
    abrev = models.TextField(max_length="10")
    web = models.URLField(blank=True)
    notes = models.TextField(help_text="Escriu una nota ", verbose_name="Notes", blank=True)
    responsable = models.ForeignKey(Usuaris)

    def __unicode__(self):
        return self.nom
    class Meta:
        ordering = ["nom"]




class Usuaris_Projectes(models.Model):
    usuari = models.ForeignKey(Usuaris)
    projecte = models.ForeignKey(Projectes)

    def __unicode__(self):
        return u'%s %s | %s ' %(self.usuari.nom, self.usuari.cognoms,self.projecte.abrev)

    class Meta:
        unique_together = [('usuari','projecte')]


