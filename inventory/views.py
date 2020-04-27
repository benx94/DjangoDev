from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import InventoryAddForm, InventoryAddNewForm, ParagraphErrorList
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError
from .models import Materiel, Owner, Test
import socket, platform


"""class inventoryAddNew(CreateView):
 model = Test
 fields = '__all__'

class inventoryUpdate(UpdateView):
 model = Test
 fields = ['login','nom','prenom','telephone']

class inventoryDelete(DeleteView):
 model = Test
 success_url = reverse_lazy('inventory')"""

def index(request):
    return render(request, 'inventory/index.html')

def inventory_index(request):
    inventaires = Test.objects.all()
    paginator = Paginator(inventaires, 9)
    page = request.GET.get('page')
    try:
        inventaires = paginator.page(page)
    except PageNotAnInteger:
        inventaires = paginator.page(1)
    except EmptyPage:
        inventaires = paginator.page(paginator.num_pages)
    inventairesData = {'inventaires': inventaires, 'paginate': True}
    return render(request, 'inventory/inventoryIndex.html', inventairesData)

def materiel_index(request):
    inventaires = Test.objects.all()
    paginator = Paginator(inventaires, 9)
    page = request.GET.get('page')
    try:
        inventaires = paginator.page(page)
    except PageNotAnInteger:
        inventaires = paginator.page(1)
    except EmptyPage:
        inventaires = paginator.page(paginator.num_pages)
    inventairesData = {'inventaires': inventaires, 'paginate': True}
    return render(request, 'inventory/materielIndex.html', inventairesData)

def inventory_add(request):
    context = {'machineName': socket.gethostname(), 'ipUser': socket.gethostbyname(socket.gethostname()), 'message': "Nouvel inventaire ajouté"}
    # another chance to get machineName: platform.node()
    if request.method == 'POST':
        form = InventoryAddForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            login = form.cleaned_data['login']
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            telephone = form.cleaned_data['telephone']
            test = Test.objects.create(
                machine=context['machineName'],
                ip=context['ipUser'],
                login=login,
                nom=nom,
                prenom=prenom,
                telephone=telephone
            )
            return render(request, 'inventory/confirm.html', context)

    else:
        data = {'login': platform.node()}
        form = InventoryAddForm(data)

    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'inventory/inventoryAdd.html', context)

def inventory_addnew(request):
    context = {'message': "Nouvel inventaire ajouté"}
    if request.method == 'POST':
        form = InventoryAddNewForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            machine = form.cleaned_data['machine']
            ip = form.cleaned_data['ip']
            login = form.cleaned_data['login']
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            telephone = form.cleaned_data['telephone']
            test = Test.objects.create(
                machine=machine,
                ip=ip,
                login=login,
                nom=nom,
                prenom=prenom,
                telephone=telephone
            )
            return render(request, 'inventory/confirm.html', context)

    else:
        form = InventoryAddNewForm()
    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'inventory/inventoryAddNew.html', context)

def inventory_update(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    context = {'testData': test, 'message': "Inventaire mis à jour"}
    if request.method == 'POST':
        form = InventoryAddForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            test.login = form.cleaned_data['login']
            test.nom = form.cleaned_data['nom']
            test.prenom = form.cleaned_data['prenom']
            test.telephone = form.cleaned_data['telephone']
            test.save()
            return render(request, 'inventory/confirm.html', context)
    else:
        data = {'login': test.login, 'nom': test.nom, 'prenom': test.prenom, 'telephone': test.telephone}
        form = InventoryAddForm(data)

    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'inventory/inventoryUpdate.html', context)

def inventory_delete(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    context = {'testData': test, 'message': "Inventaire supprimé"}
    if request.method == 'POST':
        form = InventoryAddNewForm(request.POST, error_class=ParagraphErrorList)
        test.delete()
        return render(request, 'inventory/confirm.html', context)
    else:
        form = InventoryAddNewForm()

    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'inventory/inventoryDelete.html', context)
