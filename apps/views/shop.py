from django.shortcuts import render


def index(request):
    context = {
        "url":"Asd"
    }
    return render(request, 'pages/shop/index.html', context=context)
