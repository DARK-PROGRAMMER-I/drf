from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        print(serializer)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title
            serializer.save(content = content)
        
    
product_create_view = ProductCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
product_detail_view = ProductDetailAPIView.as_view()

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_list_create_view = ProductListCreateApiView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    def perform_update(self, serializer):
        instance = serializer.save()
        
        # check if content value is not none
        if not instance.content:
            instance.content = instance.title
            
product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    
product_destroy_view = ProductDestroyAPIView.as_view()

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request , *args, **kwargs):
        pk = kwargs.get('pk')
        return self.list(request, *args, **kwargs)
product_mixin_view = ProductMixinView.as_view()





@api_view(['GET', 'POST'])
def product_alt_view(request, pk = None):
    method  = request.method
    
    if method == 'GET':
        if not pk == None:
            product = Product.objects.get(id = pk)
            serializer = ProductSerializer(product, many= False)
            
            return Response(serializer.data)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many = True)
            return Response(serializer.data)
        
    elif method == 'POST':
        product = Product.objects.get(id = pk)
        
        serializer = ProductSerializer(product , data= request.data)
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)
    