from django.shortcuts import render, redirect
from .models import Flight
from .forms import OfferForm


# Create your views here.


def Home(request):
    return render(request, "Adoffer/welcome1.html", {})

def Offer(request):
    context = {}
    if request.POST:
        form = OfferForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            form.save()
            return redirect('home')
        else:
            context['Offer_form'] = form
    else:
        form = OfferForm()
        context['Offer_form'] = form

    return render(request,"AdOffer/Offer.html", context)


def AdminProcess(request):
    context={

        'Offers': Flight.objects.filter(is_approved=False, is_rejected=False)
    }
        

    return render(request, "AdOffer/admin.html", context)


def Profile(request):
    context={
        "my_offer": Flight.objects.filter(user=request.user)

    }
    return render (request, 'AdOffer/profile.html', context)


def AcceptOfferAdmin(request,pk):
    offer = Flight.objects.get(id=pk)
    offer.is_approved = True
    offer.save()
    return redirect('offer')

def RejectOfferAdmin(request,pk):
    offer = Flight.objects.get(id=pk)
    offer.is_rejected = True
    offer.save()
    return redirect('offer')

def Payment(request):
    return render(request, 'AdOffer/payment.html')

def Passenger(request):
    return render(request, 'AdOffer/numberofpassenger.html')

def ConfirmBooking(request):
    return render(request, 'AdOffer/bookingconfirmed.html')

def Search(request):
    return render(request, 'AdOffer/searchresult1.html')
