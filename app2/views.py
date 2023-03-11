from django.shortcuts import render

# Create your views here.
def app2_page(request):
    return render(request,'app2_page.html')
def app1_page(request):
    return render(request,'app1_page.html')