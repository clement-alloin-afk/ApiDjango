from asyncio.windows_events import NULL
from gettext import NullTranslations
from rest_framework.response import Response
from rest_framework.decorators import api_view

from myapp.models import Family, User, Repas, Category, Stockage, Produit
from myapp.serializers import FamilySerializer, UserSerializer, RepasSerializer, CategorySerializer, StockageSerializer,ProduitSerializer
from rest_framework import generics

#Familles
class FamilyList(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class FamilyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class FamilyMembresList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.filter(refFamily=self.kwargs['pkF'])

#User
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def FamilyCode(request, code):
    fam = Family.objects.get(code=code)
    serializer = FamilySerializer(fam)
    return Response(serializer.data)

#Repas
class RepasList(generics.ListCreateAPIView):
    queryset = Repas.objects.all()
    serializer_class = RepasSerializer

class RepasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repas.objects.all()
    serializer_class = RepasSerializer

class FamilyRepasList(generics.ListCreateAPIView):
    serializer_class = RepasSerializer
    def get_queryset(self):
        return Repas.objects.filter(refFamily=self.kwargs['pkF'])

class FamilyRepasDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RepasSerializer
    def get_queryset(self):
        return Repas.objects.filter(refFamily=self.kwargs['pkF'],id=self.kwargs['pk'])

#Category
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FamilyCategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.filter(refFamily=self.kwargs['pkF'])

class FamilyCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.filter(refFamily=self.kwargs['pkF'],id=self.kwargs['pk'])

#Stockage
class StockageList(generics.ListCreateAPIView):
    queryset = Stockage.objects.all()
    serializer_class = StockageSerializer

class StockageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stockage.objects.all()
    serializer_class = StockageSerializer

class FamilyStockageList(generics.ListCreateAPIView):
    serializer_class = StockageSerializer
    def get_queryset(self):
        return Stockage.objects.filter(refFamily=self.kwargs['pkF'])

class FamilyStockageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StockageSerializer
    def get_queryset(self):
        return Stockage.objects.filter(refFamily=self.kwargs['pkF'],id=self.kwargs['pk'])

#Produit
class ProduitList(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ProduitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class FamilyProduitList(generics.ListCreateAPIView):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        stockList = Stockage.objects.filter(refFamily=self.kwargs['pkF'])
        listeIdStock = []
        for stock in stockList :
            print(stock.id)
            listeIdStock.append(stock.id)
            # listeProduit.append(Produit.objects.filter(refStockage=stock.id))
        return Produit.objects.filter(refStockage__in=listeIdStock)

# class FamilyProduitDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProduitSerializer
#     def get_queryset(self):
#         stockF = Stockage.objects.filter(refFamily=self.kwargs['pkF'])
#         return Produit.objects.filter(refFamily=self.kwargs['pkF'],id=self.kwargs['pk'])