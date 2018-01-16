from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from my_site.apps.price.models import Price
from .forms import PriceForm

# Create your views here.
def price(request):
    prices = Price.objects.all()
    contex = {"prices": prices}
    return  render(request, "price.html", contex)




def add_price(request, id=None):

    item = get_object_or_404(Price)
    form = PriceForm(request.POST or None ,instance=item)

    if request.method == 'POST':
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
        else:
            form = PriceForm()
        return HttpResponseRedirect('/price/')
