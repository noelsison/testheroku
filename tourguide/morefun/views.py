# Create your views here.
from django.shortcuts import render_to_response

def view_index(request):
    return render_to_response("index.html")