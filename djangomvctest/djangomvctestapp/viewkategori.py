from django.http.response import HttpResponse
from django.shortcuts import  render_to_response
from models import Kategori


def get_kategori_list1(request):
    kategorilist = Kategori.objects.all()
    return render_to_response("viewkategori1.html",{'kategorilist':kategorilist})

def get_kategori_list2(request):
    kategorilist = Kategori.objects.all()
    return render_to_response("viewkategori2.html",{'kategorilist':kategorilist})

