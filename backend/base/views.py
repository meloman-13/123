from rest_framework.response import Response
from rest_framework.decorators import api_view

from .products import products
from .models import Product
from .serializers import ProductSerializer


@api_view(["GET"])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(products, many=False)

    return Response(serializer.data)
