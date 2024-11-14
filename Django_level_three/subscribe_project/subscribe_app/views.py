from django.shortcuts import render
from subscribe_app.models import Customer


# Create your views here.
def index(request):
    return render(request, 'subscribe_app/index.html')

def Customers(request):
    Customers_list = Customer.objects.order_by('first_name')
    Customers_dict = {'Customers': Customers_list}
    return render(request, 'subscribe_app/Customers.html', context=Customers_dict)

def subscribe(request):
    form = NewsubscriberSubscriber()
    
    if request.method == 'POST':
        form = Newsubscriber(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error: From Invalid")
            
    return render(request, 'subscribe_app/subscribe.html', {'form':form})
        
            
        