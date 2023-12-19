from django.urls import path
from . import views
from .views import CatogriesView,CatogriesDetails
from Reviews.views import Reviews

urlpatterns = [
    path('',views.home,name="Home" ),
    path('Catogries',views.catogries,name="Catogries" ),
    path('Catogries',views.CatogriesView.as_view(),name="Catogries"),
    path('Catogries/<int:pk>',views.CatogriesDetails.as_view(),name="Catogries-Details"),
    path('Catogries/<int:pk>/review',Reviews.as_view(),name="Review"),
]
