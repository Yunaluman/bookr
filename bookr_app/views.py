from django.http import HttpResponse
from django.shortcuts import render
from backoffice.models import Livre, LivreType, LivreStatus
from django.db.models import Max


def index(request):
    """Vue pour afficher toutes les requêtes demandées"""

    # 1. Liste de tous les livres créés
    tous_les_livres = Livre.objects.all()

    # 2. Livres qui commencent par "L"
    livres_commencent_L = Livre.objects.filter(nom__startswith="L")

    # 3. Livres qui contiennent "Misérables" dans le titre
    livres_avec_miserables = Livre.objects.filter(nom__icontains="Misérables")

    # 4. Livres dont le prix est >= 10
    livres_prix_gte_10 = Livre.objects.filter(prix__gte=10)

    # 5. Livres dont le prix >= 10 ET statut "toujours publié"
    livres_prix_10_et_publie = Livre.objects.filter(
        prix__gte=10,
        livre_status__status="toujours publié"
    )

    # 6. Livre avec le prix le plus élevé
    livre_prix_max = Livre.objects.order_by('-prix').first()
    # Alternative: livre_prix_max = Livre.objects.aggregate(Max('prix'))

    # 7. Liste des statuts de nos livres
    statuts_livres = LivreStatus.objects.all()

    # 8. Nombre total de livres
    nombre_total_livres = Livre.objects.count()

    context = {
        'tous_les_livres': tous_les_livres,
        'livres_commencent_L': livres_commencent_L,
        'livres_avec_miserables': livres_avec_miserables,
        'livres_prix_gte_10': livres_prix_gte_10,
        'livres_prix_10_et_publie': livres_prix_10_et_publie,
        'livre_prix_max': livre_prix_max,
        'statuts_livres': statuts_livres,
        'nombre_total_livres': nombre_total_livres,
    }

    return render(request, 'bookr_app/index.html', context)
