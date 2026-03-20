from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from backoffice.models import Auteur, Livre, LivreType, LivreStatus
from backoffice.forms import AuteurForm, LivreForm


# ── Dashboard (les 8 requêtes exercice) ───────────────────────────────────────

def index(request):
    context = {
        'tous_les_livres': Livre.objects.select_related('auteur', 'livre_type', 'livre_status'),
        'livres_commencent_L': Livre.objects.filter(nom__startswith="L"),
        'livres_avec_miserables': Livre.objects.filter(nom__icontains="Misérables"),
        'livres_prix_gte_10': Livre.objects.filter(prix__gte=10),
        'livres_prix_10_et_publie': Livre.objects.filter(prix__gte=10, livre_status__status="toujours publié"),
        'livre_prix_max': Livre.objects.order_by('-prix').first(),
        'statuts_livres': LivreStatus.objects.all(),
        'nombre_total_livres': Livre.objects.count(),
        'valeur_catalogue': Livre.objects.aggregate(total=Sum('prix'))['total'] or 0,
        'nombre_auteurs': Auteur.objects.count(),
    }
    return render(request, 'backoffice/index.html', context)


# ── CRUD Livres ───────────────────────────────────────────────────────────────

def livres_list(request):
    livres = Livre.objects.select_related('auteur', 'livre_type', 'livre_status')
    return render(request, 'backoffice/livres/list.html', {'livres': livres})


def livre_create(request):
    form = LivreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('backoffice:livres_list')
    return render(request, 'backoffice/livres/form.html', {'form': form, 'titre': 'Ajouter un livre'})


def livre_update(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    form = LivreForm(request.POST or None, instance=livre)
    if form.is_valid():
        form.save()
        return redirect('backoffice:livres_list')
    return render(request, 'backoffice/livres/form.html', {'form': form, 'titre': f'Modifier — {livre.nom}', 'livre': livre})


def livre_delete(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == 'POST':
        livre.delete()
        return redirect('backoffice:livres_list')
    return render(request, 'backoffice/livres/confirm_delete.html', {'objet': livre, 'type': 'livre'})


# ── CRUD Auteurs ──────────────────────────────────────────────────────────────

def auteurs_list(request):
    auteurs = Auteur.objects.prefetch_related('livres')
    return render(request, 'backoffice/auteurs/list.html', {'auteurs': auteurs})


def auteur_create(request):
    form = AuteurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('backoffice:auteurs_list')
    return render(request, 'backoffice/auteurs/form.html', {'form': form, 'titre': 'Ajouter un auteur'})


def auteur_update(request, pk):
    auteur = get_object_or_404(Auteur, pk=pk)
    form = AuteurForm(request.POST or None, instance=auteur)
    if form.is_valid():
        form.save()
        return redirect('backoffice:auteurs_list')
    return render(request, 'backoffice/auteurs/form.html', {'form': form, 'titre': f'Modifier — {auteur}', 'auteur': auteur})


def auteur_delete(request, pk):
    auteur = get_object_or_404(Auteur, pk=pk)
    if request.method == 'POST':
        auteur.delete()
        return redirect('backoffice:auteurs_list')
    return render(request, 'backoffice/auteurs/confirm_delete.html', {'objet': auteur, 'type': 'auteur'})
