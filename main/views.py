from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'DENIM SHIRT WITH PATCH POCKETS',
        'price': 629900,
        'description': 'Shirt with a Johnny collar and long sleeves. Featuring front patch pockets and a button-up front with snap buttons.',
        'size': 'S, M, L, XL, XXL'
    }

    return render(request, "main.html", context)