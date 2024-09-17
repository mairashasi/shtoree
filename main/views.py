from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductForm
from main.models import Product

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
        'product_rates' : product_rating

    }

    return render(request, "main.html", context)

def create_product_rating(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_rating.html", context)
