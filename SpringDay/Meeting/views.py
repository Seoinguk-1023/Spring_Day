from django.shortcuts import render

# Create your views here.
def meet(request):
    return render(request,'meet.html')