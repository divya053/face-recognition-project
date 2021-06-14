from django.urls import path
from . import views

urlpatterns = [
    
    path('/face_dect',views.detect_face())

]
