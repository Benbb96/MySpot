from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_date = models.DateTimeField('date de création', auto_now_add=True, editable=False)
    modified_date = models.DateTimeField('date de dernière modification', auto_now=True)

    class Meta:
        abstract = True

class Groupe(BaseModel):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return 'Groupe "{0}"'.format(self.nom)

class Spotteur(BaseModel):
    user = models.OneToOneField(User)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars/')
    groupes = models.ManyToManyField(Groupe, blank=True)

    def __str__(self):
        return self.user.username

class Spot(BaseModel):
    spotteur = models.ForeignKey(Spotteur, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    lat = models.FloatField('latitude')
    lng = models.FloatField('longitude')
    groupes_de_partage = models.ManyToManyField(Groupe, blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return 'Spot "{0}"'.format(self.nom)

class Photo(BaseModel):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    auteur = models.ForeignKey(Spotteur, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=240)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return "Photo de {0} sur le {1}".format(self.auteur, self.spot)