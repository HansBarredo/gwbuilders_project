import pytest
from projects.models import Project  # Replace 'myapp' with the actual app name

@pytest.mark.django_db
def test_project_model():
    # example data input
    project1 = Project.objects.create(
        title="Community Center",
        address="123 Main St",
        city="Metropolis",
        state="Gotham",
        zipcode="54321",
        short_description="test-description",
        description="test-description",
        completion="2024-12-31",
        photo_main="photos/2024/12/31/main.jpg",
        is_published=True
    )

    project_from_db = Project.objects.get(id=project1.id)

    assert project_from_db.title == "Community Center", "Title should match the created instance"
    assert project_from_db.photo_main == "photos/2024/12/31/main.jpg", "Photo_main should match the created instance"