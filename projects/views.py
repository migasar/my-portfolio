from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Project


def index(request):
    # return HttpResponse("Hello, world. You're at the projects index.")
    # project_list = Project.objects.all()
    # output = ', '.join([p.title for p in project_list])
    # return HttpResponse(output)
    # project_list = Project.objects.all()
    # template = loader.get_template('polls/index.html')
    # context = {'project_list': project_list}
    # return HttpResponse(template.render(context, request))
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'projects/index.html', context)


def detail(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)
