from django.shortcuts import render
from search.models import *

# Create your views here.
def home(request):

    if request.method == 'POST':
        search_keyword = request.POST['input']

        if not search_keyword:
            return render(request, 'index.html')

        items = Dish.objects.all()
        searched_items = items.filter(name__icontains=search_keyword)

        return render(request, 'index.html', {'items':searched_items, 'formdata':search_keyword})

    return render(request, 'index.html')