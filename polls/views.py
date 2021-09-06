from django.shortcuts import render



# Create your views here.
def home(request):
    if(request.POST.get('submit')):
        return render(request,'polls/home.html')


    