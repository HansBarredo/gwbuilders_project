import pytest
from django.test import RequestFactory
from django.urls import reverse
from contacts.views import contact

@pytest.mark.django_db
def test_contact_get_view():
    path = reverse('contacts')  
    request = RequestFactory().get(path)
    response = contact(request)
   
    assert response.status_code == 200