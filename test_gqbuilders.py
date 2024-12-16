import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_index(client):
    # Reverse URL resolution
    url = reverse('index')
    assert url == '/'  # Ensure URL resolves correctly

    # Simulate a GET request
    response = client.get(url)

    # Assert status code
    assert response.status_code == 200
