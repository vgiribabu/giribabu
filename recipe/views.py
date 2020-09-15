from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('recipe:index'))
        else:
            return HttpResponse('Invalid credentials')
    return render(request, 'recipe/login.html')


def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
            email = request.POST['email'],
        )
        return HttpResponseRedirect(reverse('recipe:login'))
    return render(request, 'recipe/register.html')


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('recipe:login'))


def index(request):
    recipe = Recipe.objects.all()
    context = {'recipe': recipe}
    return render(request, 'recipe/index.html', context)


def detail(request, recipe_id):
    check = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipe/detail.html", {'check': check})


@login_required(login_url='/recipe/login')
def create(request):
    if request.method == "POST":
        Recipe.objects.create(
                creater = request.POST['creater'],
                name = request.POST['name'],
                ingredients = request.POST['ingredients'],
                process = request.POST['process'],
                date = timezone.now()

        )
        return HttpResponseRedirect(reverse('recipe:index'))
    return render(request, 'recipe/create.html')

