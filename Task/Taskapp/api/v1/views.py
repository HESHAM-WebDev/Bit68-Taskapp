from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from ...models import Product


@api_view(["GET", "POST"]) # tells django that this is a type of rest view
def Test(request):
    if request.method == 'POST':
        return Response(
                       {'message': 'Post request-Response'}, status=status.HTTP_201_CREATED)
    return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def Create_Product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def View_Product(request):
    products = Product.objects.all()
    serializer = ProductSerializer(instance=products, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)