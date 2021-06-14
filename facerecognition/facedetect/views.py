from django.shortcuts import render
from . import face

# Create your views here.



def detect_face():
    return face.recognition()
