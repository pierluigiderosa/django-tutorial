from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from recipes.models import Food

def food_list(request):
    food = Food.objects.all()
    return render_to_response('recipes/food_list.html',
                              {'object_list': food}, context_instance=RequestContext(request))