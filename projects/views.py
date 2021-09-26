from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def detail(request, project_id):
    context = {'project_id': project_id}
    return render(request, 'detail.html', context)
