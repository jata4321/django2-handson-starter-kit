from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {'title':'Title page'}
    return render(request, 'allpages/index.html', context)

def about_view(request):
    context = {'title':'About Us'}
    return render(request, 'allpages/about.html', context)
    
def privacy_view(request):
    context = {'title':'Privacy Policy'}
    return render(request, 'allpages/privacy.html', context)