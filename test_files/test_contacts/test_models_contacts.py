import pytest
from mixer.backend.django import mixer

@pytest.mark.django_db
class TestModels:
    def test_title(self):
        contact = mixer.blend('contacts.Contact', title = "hans")
        assert contact.title == "hans"