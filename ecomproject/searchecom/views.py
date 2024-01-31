from django.shortcuts import render
from ecomapp.models import Product
from django.db.models import Q
# Create your views here.
def SearchRes(request):
    product=None
    query=None
    if 'q' in request.GET:
        query = request.GET.get('q')
        product = Product.objects.all().filter(Q(name__icontains=query) | Q(desc__icontains=query))
        print(f"SQL query: {str(product.query)}")

    return render(request, 'search.html', {'query': query, 'product': product})
