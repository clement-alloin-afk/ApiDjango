from asyncio.windows_events import NULL
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from myapp.models import Family, User, Repas, Category, Stockage, Produit, Liste, Tache, LigneRepas, LigneListe
from myapp.serializers import ( FamilySerializer, UserSerializer, RepasSerializer, CategorySerializer, StockageSerializer,ProduitSerializer,
ListeSerializer,TacheSerializer, LigneRepasSerializer, LigneListeSerializer )
from rest_framework import generics


#Familles
class FamilyList(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [IsAuthenticated]

class FamilyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class FamilyMembresList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return User.objects.filter(refFamily=self.kwargs['pkF'])

#User
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def FamilyCode(request, code):
    fam = Family.objects.get(code=code)
    serializer = FamilySerializer(fam)
    permission_classes = [IsAuthenticated]
    return Response(serializer.data)

#Repas
class RepasList(generics.ListCreateAPIView):
    queryset = Repas.objects.all()
    serializer_class = RepasSerializer
    permission_classes = [IsAuthenticated]

class RepasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repas.objects.all()
    serializer_class = RepasSerializer
    permission_classes = [IsAuthenticated]

class FamilyRepasList(generics.ListCreateAPIView):
    serializer_class = RepasSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Repas.objects.filter(refFamily=self.kwargs['pkF'])

class FamilyRepasDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RepasSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Repas.objects.filter(refFamily=self.kwargs['pkF'],id=self.kwargs['pk'])

#Category
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class FamilyCategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Category.objects.filter(refFamily=self.kwargs['pkF'])

class FamilyCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Category.objects.filter(refFamily=self.kwargs['pkF'],id=self.kwargs['pk'])

#Stockage
class StockageList(generics.ListCreateAPIView):
    queryset = Stockage.objects.all()
    serializer_class = StockageSerializer

class StockageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stockage.objects.all()
    serializer_class = StockageSerializer
    permission_classes = [IsAuthenticated]

class FamilyStockageList(generics.ListCreateAPIView):
    serializer_class = StockageSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Stockage.objects.filter(refFamily=self.kwargs['pkF'])

class FamilyStockageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StockageSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Stockage.objects.filter(refFamily=self.kwargs['pkF'],id=self.kwargs['pk'])

class StockageListProduit(generics.ListCreateAPIView):
    serializer_class = ProduitSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Produit.objects.filter(refStockage=self.kwargs['pk'])

#Produit
class ProduitList(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ProduitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

    def perform_update(self, serializer):
        produitToUpdate = Produit.objects.get(id=self.kwargs['pk'])
        newQuantity = serializer.validated_data.get('quantity')
        #Check si la quantité est mis à jour et si le produit à l'option pour l'ajout auto
        if (newQuantity != None and produitToUpdate.isQuantityMin):
            #Check si la quantité est diminué et si elle est égale à la quantité min
            if (newQuantity < produitToUpdate.quantity and newQuantity == produitToUpdate.quantityMin) :
                famille = produitToUpdate.refStockage.refFamily
                #Check si une liste de course à déjà le produit, maj de cette ligne si c'est le cas, sinon nouvelle ligne dans la première liste
                ligne = LigneListe.objects.filter(refProduit=produitToUpdate).first()
                if (ligne != None ):
                    if (ligne.quantity < produitToUpdate.quantityAutoAdd) :
                        ligne.quantity = produitToUpdate.quantityAutoAdd
                        ligne.autoAdd = True
                        ligne.save()
                else :
                    #Première liste de course de la famille
                    print("Add to course : ",produitToUpdate.quantityAutoAdd)
                    liste = Liste.objects.filter(category='Course', refFamily=famille).first()
                    LigneListe.objects.create(
                    refListe=liste,
                    refProduit=produitToUpdate,
                    mesure= "Test",
                    quantity= produitToUpdate.quantityAutoAdd,
                    autoAdd= True,
                    )

        serializer.save()

class AddProduitFromCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        produitToUpdate = Produit.objects.get(id=self.kwargs['pk'])
        refStock = serializer.validated_data.get('refStockage')
        # Produit n'a pas de stockage ou Ajout dans le même stock
        if (produitToUpdate.refStockage == None or produitToUpdate.refStockage.id == refStock.id) :
            serializer.validated_data["quantity"] = serializer.validated_data["quantity"] + produitToUpdate.quantity
            print("save",serializer.validated_data["quantity"])
            serializer.save()

        # Ranger le produit dans un autre stock qu'actuellement : créer un nouveau produit dans ce stock si aucun n'a déjà le même nom, sinon modifier l'existant
        else :
            produitDansNouvStock = Produit.objects.filter(refStockage=refStock.id, nom=produitToUpdate.nom)
            # Nouvel objet dans ce stockage
            if (len(produitDansNouvStock) == 0 ) : 
                Produit.objects.create(
                nom=produitToUpdate.nom,
                quantity= serializer.validated_data["quantity"],
                quantityMin= 0,
                isQuantityMin= False,
                quantityAutoAdd= 0,
                description= "",
                refStockage= refStock,
                refCategory= produitToUpdate.refCategory,
            )
            else: 
                produitDansNouvStock[0].quantity = serializer.validated_data["quantity"] + produitDansNouvStock[0].quantity
                produitDansNouvStock[0].save()



class FamilyProduitList(generics.ListCreateAPIView):
    serializer_class = ProduitSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        stockList = Stockage.objects.filter(refFamily=self.kwargs['pkF'])
        listeIdStock = []
        for stock in stockList :
            listeIdStock.append(stock.id)
            # listeProduit.append(Produit.objects.filter(refStockage=stock.id))
        return Produit.objects.filter(refStockage__in=listeIdStock)

# class FamilyProduitDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProduitSerializer
#     def get_queryset(self):
#         stockF = Stockage.objects.filter(refFamily=self.kwargs['pkF'])
#         return Produit.objects.filter(refFamily=self.kwargs['pkF'],id=self.kwargs['pk'])

#Liste
class ListeList(generics.ListCreateAPIView):
    queryset = Liste.objects.all()
    serializer_class = ListeSerializer

class ListeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Liste.objects.all()
    serializer_class = ListeSerializer

class FamilyListeList(generics.ListCreateAPIView):
    serializer_class = ListeSerializer
    def get_queryset(self):
        return Liste.objects.filter(refFamily=self.kwargs['pkF'])

#Tache
class TacheList(generics.ListCreateAPIView):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer

class TacheDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer

class ListeTacheList(generics.ListCreateAPIView):
    serializer_class = TacheSerializer
    
    def get_queryset(self):
        return Tache.objects.filter(refListe=self.kwargs['pk'])

#LigneListe
class LigneListeList(generics.ListCreateAPIView):
    queryset = LigneListe.objects.all()
    serializer_class = LigneListeSerializer

    def perform_create(self, serializer):
        if (serializer.validated_data.get('refProduit') == None) :
            createdProduit = Produit.objects.create(
                nom=serializer.validated_data.get('nomProdOptional'),
                quantity= 0,
                quantityMin= 0,
                isQuantityMin= False,
                quantityAutoAdd= 0,
                description= "",
            )
            print(createdProduit.id)
            serializer.validated_data["refProduit"] = createdProduit
            
        serializer.save()

class LigneListeId(generics.ListCreateAPIView):
    serializer_class = LigneListeSerializer
    
    def get_queryset(self):
        return LigneListe.objects.filter(refListe=self.kwargs['pk'])

class LigneListeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LigneListe.objects.all()
    serializer_class = LigneListeSerializer

#LigneRepas
class LigneRepasList(generics.ListCreateAPIView):
    queryset = LigneRepas.objects.all()
    serializer_class = LigneRepasSerializer

class LigneRepasId(generics.ListCreateAPIView):
    serializer_class = LigneRepasSerializer
    
    def get_queryset(self):
        return LigneRepas.objects.filter(refRepas=self.kwargs['pk'])

class LigneRepasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LigneRepas.objects.all()
    serializer_class = LigneRepasSerializer
