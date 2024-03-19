from django.urls import path, include
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from . import views

#
# router = DefaultRouter()
# router.register(r'inventory', InventoryViewset)
#
urlpatterns = [
    path('', views.alldata),
    path("<int:id>/",views.singledata),
    path("<str:cat>/",views.browse_cat)
]
