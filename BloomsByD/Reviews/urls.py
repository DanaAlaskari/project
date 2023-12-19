from django.urls import path
from . import views
from .views import Reviews , ReviewList


urlpatterns = [
    path('',views.home,name="Home" ),
    path('addReview',Reviews.as_view(),name="Review"),
    path('Reviews',ReviewList.as_view(),name="ReviewList"),
    
]
 