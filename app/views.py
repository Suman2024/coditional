from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':12,'b':13,'c':24}
    return render(request,'conditional.html',context=d)