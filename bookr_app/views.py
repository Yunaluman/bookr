from django.shortcuts import render, get_object_or_404
from backoffice.models import Auteur, Livre, LivreType, LivreStatus
from django.db.models import Sum


def index(request):
    query = request.GET.get('q', '').strip()
    genre_id = request.GET.get('genre', '')

    livres = Livre.objects.select_related('auteur', 'livre_type', 'livre_status')
    if query:
        livres = livres.filter(nom__icontains=query)
    if genre_id:
        livres = livres.filter(livre_type_id=genre_id)

    tous_les_types = LivreType.objects.all()
    nombre_total_livres = Livre.objects.count()
    valeur_catalogue = Livre.objects.aggregate(total=Sum('prix'))['total'] or 0
    nombre_auteurs = Auteur.objects.count()
    nombre_types = tous_les_types.count()

    context = {
        'livres': livres,
        'tous_les_types': tous_les_types,
        'query': query,
        'genre_id': int(genre_id) if genre_id else None,
        'nombre_total_livres': nombre_total_livres,
        'valeur_catalogue': valeur_catalogue,
        'nombre_auteurs': nombre_auteurs,
        'nombre_types': nombre_types,
    }
    return render(request, 'bookr_app/index.html', context)


def auteurs_list(request):
    nationalite = request.GET.get('nationalite', '').strip()
    auteurs = Auteur.objects.prefetch_related('livres')
    if nationalite:
        auteurs = auteurs.filter(nationalite=nationalite)
    nationalites = (
        Auteur.objects.exclude(nationalite='')
        .values_list('nationalite', flat=True)
        .distinct()
        .order_by('nationalite')
    )
    return render(request, 'bookr_app/auteurs.html', {
        'auteurs': auteurs,
        'nationalites': nationalites,
        'nationalite_active': nationalite,
    })


def auteur_detail(request, auteur_id):
    auteur = get_object_or_404(Auteur, pk=auteur_id)
    livres = auteur.livres.select_related('livre_type', 'livre_status')
    return render(request, 'bookr_app/auteur_detail.html', {
        'auteur': auteur,
        'livres': livres,
    })
