from rest_framework.response import Response 
from products.models import Product
# from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from products.serializers  import ProductSerializer
# Create your views here.
@api_view(["POST"])
def api_home(request, *args, **kwargs ):
    serializer = ProductSerializer(data= request.data)
    if serializer.is_valid(raise_exception= True):
        instance = serializer.save()
        print(instance)
        data = serializer.data
          
  
        return Response(data)
    return Response({"invalid":"Not a good data"})

