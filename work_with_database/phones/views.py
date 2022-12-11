from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort == 'name':
        context = {
            'phones': Phone.objects.order_by('name').all()
        }
    elif sort == 'min_price':
        context = {
            'phones': Phone.objects.order_by('price').all()
        }
    elif sort == 'max_price': #.reverse() или Phone.objects.order_by('-price').all()
        context = {
            'phones': Phone.objects.order_by('price').reverse().all()
        }
    else:
        context = {
            'phones': Phone.objects.order_by('id').all()
        }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print('slug: ', slug)
    context = {
        'phones': Phone.objects.filter(slug__contains=slug)
    }
    return render(request, template, context)