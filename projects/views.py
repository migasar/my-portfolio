# from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# from django.template import loader
# from django.http import Http404
# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404
# from django.urls import reverse
from django.views import generic

from .models import Project


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """ Return all published projects. """
        return Project.objects.all()


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'


# def index(request):
#     # return HttpResponse("Hello, world. You're at the projects index.")
#     # project_list = Project.objects.all()
#     # output = ', '.join([p.title for p in project_list])
#     # return HttpResponse(output)
#     # project_list = Project.objects.all()
#     # template = loader.get_template('polls/index.html')
#     # context = {'project_list': project_list}
#     # return HttpResponse(template.render(context, request))
#     project_list = Project.objects.all()
#     context = {'project_list': project_list}
#     return render(request, 'projects/index.html', context)


# def detail(request, project_id):
#     # return HttpResponse("You're looking at project %s." % project_id)
#     # try:
#     #     project = Project.objects.get(pk=project_id)
#     # except Project.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'projects/detail.html', {'project': project})
#     project = get_object_or_404(Project, pk=project_id)
#     return render(request, 'projects/detail.html', {'project': project})
