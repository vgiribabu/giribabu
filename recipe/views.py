from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
# Create your views here.

def index(request):
    recipe = Recipe.objects.all()
    context = {'recipe': recipe}
    return render(request, 'recipe/index.html', context)


def detail(request, recipe_id):
    check = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipe/detail.html", {'check': check})



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

