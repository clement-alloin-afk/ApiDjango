from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ( FamilyList,FamilyDetail,FamilyMembresList,FamilyRepasList,FamilyRepasDetail,
FamilyCategoryList,FamilyCategoryDetail,FamilyStockageList,FamilyStockageDetail,FamilyProduitList,FamilyListeList,
UserList,UserDetail,
RepasList,RepasDetail, 
CategoryList, CategoryDetail,
StockageList, StockageDetail,StockageListProduit,
ProduitList,ProduitDetail,
ListeList,ListeDetail,
TacheList,TacheDetail,ListeTacheList,
LigneListeList,LigneRepasList,
LigneListeDetail,LigneRepasDetail
 )
from . import views


urlpatterns = [
   path('Family/', FamilyList.as_view()),
   path('Family/<int:pk>/', FamilyDetail.as_view()),
   re_path(r'^Family/(?P<code>[A-Z0-9]{10})/$', views.FamilyCode),
   path('Family/<int:pkF>/Membres/', FamilyMembresList.as_view()),
   path('Family/<int:pkF>/Repas/', FamilyRepasList.as_view()),
   path('Family/<int:pkF>/Repas/<pk>', FamilyRepasDetail.as_view()),
   path('Family/<int:pkF>/Category/', FamilyCategoryList.as_view()),
   path('Family/<int:pkF>/Category/<pk>', FamilyCategoryDetail.as_view()),
   path('Family/<int:pkF>/Stockage/', FamilyStockageList.as_view()),
   path('Family/<int:pkF>/Stockage/<pk>', FamilyStockageDetail.as_view()),
   path('Family/<int:pkF>/Produit/', FamilyProduitList.as_view()),
   path('Family/<int:pkF>/Liste/', FamilyListeList.as_view()),
   #path('Family/<int:pkF>/Produit/<pk>', FamilyProduitDetail.as_view()),

   path('User/', UserList.as_view()),
   path('User/<pk>', UserDetail.as_view()),

   path('Repas/', RepasList.as_view()),
   path('Repas/<pk>/', RepasDetail.as_view()),

   path('Category/', CategoryList.as_view()),
   path('Category/<pk>/', CategoryDetail.as_view()),

   path('Stockage/', StockageList.as_view()),
   path('Stockage/<pk>/', StockageDetail.as_view()),
   path('Stockage/<pk>/Produit', StockageListProduit.as_view()),

   path('Produit/', ProduitList.as_view()),
   path('Produit/<pk>/', ProduitDetail.as_view()),

   path('Liste/', ListeList.as_view()),
   path('Liste/<pk>/', ListeDetail.as_view()),
   path('Liste/<pk>/Tache', ListeTacheList.as_view()),

   path('Tache/', TacheList.as_view()),
   path('Tache/<pk>/', TacheDetail.as_view()),

   path('LigneRepas/', LigneRepasList.as_view()),
   path('LigneRepas/<pk>/', LigneRepasDetail.as_view()),

   path('LigneListe/', LigneListeList.as_view()),
   path('LigneListe/<pk>/', LigneListeDetail.as_view()),
]
