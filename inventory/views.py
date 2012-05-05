# catalog

from django.views.generic import DetailView
from catalog.models import Product

class ProductView(DetailView):
    queryset = Product.objects.select_related('brand', 'manufacturer')
