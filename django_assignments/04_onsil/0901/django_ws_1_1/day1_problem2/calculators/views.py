from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'calculators/throw.html')

def catch(request):
    firstnum = request.GET.get('firstnum')
    secondnum = request.GET.get('secondnum')
    context = {
        'firstnum':firstnum,
        'secondnum':secondnum,
    }
    return render(request, 'calculators/catch.html', context)