from django.urls import reverse, resolve

class TestUrls:
    def test_projects_url(self):
        path = reverse('projects')
        assert resolve(path).view_name == 'projects'

    def test_project_url(self):
        path = reverse('project', kwargs={'project_id': 1})
        assert resolve(path).view_name == 'project'