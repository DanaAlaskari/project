from django.urls import path
from . import views
from .views import loginView, RegisterView, NoteView

urlpatterns = [
    path('', views.home, name="Home"),
    path('Login', loginView.as_view(), name="Login"),
    path('Register', RegisterView.as_view(), name="Regiter"),
    path('Note', NoteView.as_view(), name="Note"),
]