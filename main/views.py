from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_rating = Product.objects.all()

    context = {
        'nama_aplikasi': 'shtoree',
        'nama_mahasiswa': 'Maira Shasmeen Mazaya',
        'nama_kelas': 'Kelas B',
        'name': 'DENIM SHIRT WITH PATCH POCKETS',
        'price': 629900,
        'description': 'Shirt with a Johnny collar and long sleeves. Featuring front patch pockets and a button-up front with snap buttons.',
        'size': 'S, M, L, XL, XXL',
        'product_rating' : product_rating

    }

    return render(request, "main.html", context)

def create_product_rating(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_rating.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data_id = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_id), content_type="application/xml")

def show_json_by_id(request, id):
    data_id = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_id), content_type="application/json")