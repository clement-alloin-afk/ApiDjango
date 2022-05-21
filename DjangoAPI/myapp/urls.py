from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ( FamilyList,FamilyDetail,FamilyMembresList,FamilyRepasList,FamilyRepasDetail,
FamilyCategoryList,FamilyCategoryDetail,FamilyStockageList,FamilyStockageDetail,FamilyProduitList,FamilyListeList, PeremptionListForProduit,
UserList,UserDetail,
RepasList,RepasDetail, 
CategoryList, CategoryDetail,
StockageList, StockageDetail,StockageListProduit,
ProduitList,ProduitDetail,AddProduitFromCourse,
ListeList,ListeDetail,
TacheList,TacheDetail,ListeTacheList,
LigneListeList,LigneRepasList,LigneRepasId,
LigneListeDetail,LigneRepasDetail, LigneListeId,
NotificationList,NotificationDetail,FamilyNotificationList,
PeremptionList,PeremptionDetail
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
   path('Family/<int:pkF>/Notification/', FamilyNotificationList.as_view()),
   #path('Family/<int:pkF>/Produit/<pk>', FamilyProduitDetail.as_view()),

   path('User/', UserList.as_view()),
   path('User/<pk>/', UserDetail.as_view()),

   path('Repas/', RepasList.as_view()),
   path('Repas/<pk>/', RepasDetail.as_view()),

   path('Category/', CategoryList.as_view()),
   path('Category/<pk>/', CategoryDetail.as_view()),

   path('Stockage/', StockageList.as_view()),
   path('Stockage/<pk>/', StockageDetail.as_view()),
   path('Stockage/<pk>/Produit', StockageListProduit.as_view()),

   path('Produit/', ProduitList.as_view()),
   path('Produit/<pk>/', ProduitDetail.as_view()),
   path('AddProduit/<pk>/', AddProduitFromCourse.as_view()),

   path('Liste/', ListeList.as_view()),
   path('Liste/<pk>/', ListeDetail.as_view()),
   path('Liste/<pk>/Tache', ListeTacheList.as_view()),

   path('Tache/', TacheList.as_view()),
   path('Tache/<pk>/', TacheDetail.as_view()),

   path('LigneRepas/', LigneRepasList.as_view()),
   path('LigneRepasId/<pk>/', LigneRepasId.as_view()),
   path('LigneRepas/<pk>/', LigneRepasDetail.as_view()),

   path('LigneListe/', LigneListeList.as_view()),
   path('LigneListeId/<pk>/', LigneListeId.as_view()),
   path('LigneListe/<pk>/', LigneListeDetail.as_view()),

   path('PeremptionProduit/', PeremptionList.as_view()),
   path('PeremptionProduit/<pk>/', PeremptionDetail.as_view()),
   path('PeremptionProduitForProduit/<pk>/', PeremptionListForProduit.as_view()),
   
   path('Notification/', NotificationList.as_view()),
   path('Notification/', NotificationList.as_view()),
   path('Notification/<pk>/', NotificationDetail.as_view()),
]
