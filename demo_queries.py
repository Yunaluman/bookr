# -*- coding: utf-8 -*-
"""
Script de démonstration de toutes les requêtes du projet
Usage: python manage.py shell -c "exec(open('demo_queries.py', encoding='utf-8').read())"
"""
from backoffice.models import Livre, LivreType, LivreStatus

print("=" * 70)
print("DÉMONSTRATION DES REQUÊTES - PROJET BOOKR")
print("=" * 70)

# 1. Liste de tous les livres créés
print("\n1. TOUS LES LIVRES CRÉÉS")
print("-" * 70)
tous_les_livres = Livre.objects.all()
for livre in tous_les_livres:
    print(f"  • {livre.nom} - {livre.prix}€ [{livre.livre_type.genre}] ({livre.livre_status.status})")

# 2. Livres qui commencent par "L"
print("\n2. LIVRES QUI COMMENCENT PAR 'L'")
print("-" * 70)
livres_L = Livre.objects.filter(nom__startswith="L")
print(f"  Requête: Livre.objects.filter(nom__startswith='L')")
print(f"  Résultats: {livres_L.count()} livre(s)")
for livre in livres_L:
    print(f"  • {livre.nom} - {livre.prix}€")

# 3. Livres qui contiennent "Misérables" dans le titre
print("\n3. LIVRES CONTENANT 'MISÉRABLES' DANS LE TITRE")
print("-" * 70)
livres_miserables = Livre.objects.filter(nom__icontains="Misérables")
print(f"  Requête: Livre.objects.filter(nom__icontains='Misérables')")
print(f"  Résultats: {livres_miserables.count()} livre(s)")
for livre in livres_miserables:
    print(f"  • {livre.nom} - {livre.prix}€")

# 4. Livres dont le prix est >= 10
print("\n4. LIVRES DONT LE PRIX EST >= 10€")
print("-" * 70)
livres_prix_10 = Livre.objects.filter(prix__gte=10)
print(f"  Requête: Livre.objects.filter(prix__gte=10)")
print(f"  Résultats: {livres_prix_10.count()} livre(s)")
for livre in livres_prix_10:
    print(f"  • {livre.nom} - {livre.prix}€")

# 5. Livres dont le prix >= 10 ET statut "toujours publié"
print("\n5. LIVRES PRIX >= 10€ ET STATUT 'TOUJOURS PUBLIÉ'")
print("-" * 70)
livres_prix_10_publie = Livre.objects.filter(
    prix__gte=10,
    livre_status__status="toujours publié"
)
print(f"  Requête: Livre.objects.filter(prix__gte=10, livre_status__status='toujours publié')")
print(f"  Résultats: {livres_prix_10_publie.count()} livre(s)")
for livre in livres_prix_10_publie:
    print(f"  • {livre.nom} - {livre.prix}€ ({livre.livre_status.status})")

# 6. Livre avec le prix le plus élevé
print("\n6. LIVRE AVEC LE PRIX LE PLUS ÉLEVÉ")
print("-" * 70)
livre_max = Livre.objects.order_by('-prix').first()
print(f"  Requête: Livre.objects.order_by('-prix').first()")
if livre_max:
    print(f"  Résultat: {livre_max.nom} - {livre_max.prix}€")
else:
    print("  Aucun livre trouvé")

# Alternative avec aggregate
from django.db.models import Max
prix_max = Livre.objects.aggregate(Max('prix'))
print(f"  Alternative avec aggregate: {prix_max}")

# 7. Liste des statuts
print("\n7. LISTE DES STATUTS DE NOS LIVRES")
print("-" * 70)
statuts = LivreStatus.objects.all()
print(f"  Requête: LivreStatus.objects.all()")
print(f"  Résultats: {statuts.count()} statut(s)")
for status in statuts:
    print(f"  • {status.status}")

# 8. Nombre total de livres
print("\n8. NOMBRE TOTAL DE LIVRES")
print("-" * 70)
nombre_livres = Livre.objects.count()
print(f"  Requête: Livre.objects.count()")
print(f"  Résultat: {nombre_livres} livre(s)")

print("\n" + "=" * 70)
print("FIN DE LA DÉMONSTRATION")
print("=" * 70)

# Afficher quelques statistiques supplémentaires
print("\nSTATISTIQUES SUPPLÉMENTAIRES")
print("-" * 70)
from django.db.models import Avg, Min, Max, Count

stats = Livre.objects.aggregate(
    prix_moyen=Avg('prix'),
    prix_min=Min('prix'),
    prix_max=Max('prix'),
    total=Count('id')
)

print(f"  Prix moyen: {stats['prix_moyen']:.2f}€" if stats['prix_moyen'] else "  Prix moyen: N/A")
print(f"  Prix minimum: {stats['prix_min']}€" if stats['prix_min'] else "  Prix minimum: N/A")
print(f"  Prix maximum: {stats['prix_max']}€" if stats['prix_max'] else "  Prix maximum: N/A")
print(f"  Total de livres: {stats['total']}")

# Livres par type
print("\n  Livres par type:")
for livre_type in LivreType.objects.all():
    count = livre_type.livres.count()
    print(f"    • {livre_type.genre}: {count} livre(s)")

# Livres par statut
print("\n  Livres par statut:")
for status in LivreStatus.objects.all():
    count = status.livres.count()
    print(f"    • {status.status}: {count} livre(s)")

print("\n" + "=" * 70)
