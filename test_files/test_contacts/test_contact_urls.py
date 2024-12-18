from django.urls import reverse, resolve

class TestUrls:
    def test_projects_url(self):
        path = reverse('contacts')
        assert resolve(path).view_name == 'contacts'

    