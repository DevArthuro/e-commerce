from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'principal',
        'filestatic': [
            'style.css'
        ]
    }
    return render(request, "ecommerce/index.html", context)