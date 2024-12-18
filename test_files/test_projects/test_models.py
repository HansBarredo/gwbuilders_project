import pytest
from mixer.backend.django import mixer

@pytest.mark.django_db
class TestModels:
    def test_title(self):
        project = mixer.blend('projects.Project', title = "House")
        assert project.title == "House"