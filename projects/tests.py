from django.test import TestCase

# Create your tests here.

from django.urls import reverse

from .models import Project


# class ProjectModelTests(TestCase):
#     pass


def create_project(title, description, technology):
    """ Create a project
    with the given `title`, `description` and `technology`.
    """
    project = Project.objects.create(
        title=title,
        description=description,
        technology=technology,
        image='images/project1.png'
        )
    return project


class ProjectIndexViewTests(TestCase):

    def test_no_projects(self):
        """
        If no projects exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('projects:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects are available.")
        self.assertQuerysetEqual(response.context['project_list'], [])

    def test_one_project(self):
        """ Test if a project has been created. """
        project = create_project(
            title="Test project",
            description="Descriptive text of the project created for testing.",
            technology="main tech of test"
        )
        response = self.client.get(reverse('projects:index'))
        self.assertQuerysetEqual(response.context['project_list'],[project],)
