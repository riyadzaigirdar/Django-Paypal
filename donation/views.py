from django.shortcuts import render
from donation.form import DonationForm
from donation.models import Donation
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = DonationForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount']
            donation = Donation(name = name, amount = amount)
            donation.save()

            context = {
                'amount' : str(amount),
                'id': settings.PAYPAL_RECEIVER_ID
            }
            return render(request, 'paypal.html', context)

    form = DonationForm()
    
    return render(request, 'checkout.html',{'form':form})
