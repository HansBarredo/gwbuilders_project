from django.urls import reverse, resolve
from django.conf import settings

class TestUrls:
    def test_admin_url(self):
        path = reverse('admin:index')
        assert resolve(path).route == 'admin/'

    def test_index_url(self):
        path = '/'
        resolve(path) is not None
    
    def test_projects_url(self):
        path = '/projects/'
        resolve(path) is not None
    