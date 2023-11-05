from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def art(request, id):
    print(id)
    return render(request, 'articles/' + str(id) + '.html')


# Create your views here.
