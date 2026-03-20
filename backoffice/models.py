from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return f"{self.name} [{self.code}]"


class ProductItem(models.Model):
    color = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    code = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.color} [{self.code}]"


class Auteur(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
        ordering = ['nom', 'prenom']


class LivreType(models.Model):
    genre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = "Type de livre"
        verbose_name_plural = "Types de livres"


class LivreStatus(models.Model):
    status = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Statut de livre"
        verbose_name_plural = "Statuts de livres"


class Livre(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    auteur = models.ForeignKey(
        Auteur,
        on_delete=models.PROTECT,
        related_name='livres',
        null=True,
        blank=True
    )
    livre_type = models.ForeignKey(
        LivreType,
        on_delete=models.PROTECT,
        related_name='livres'
    )
    livre_status = models.ForeignKey(
        LivreStatus,
        on_delete=models.PROTECT,
        related_name='livres'
    )

    def __str__(self):
        return f"{self.nom} - {self.prix}€"

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
        ordering = ['nom']
