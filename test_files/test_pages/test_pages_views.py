import pytest
from django.urls import reverse
from django.test import Client
from projects.models import Project
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_index_view():
    image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

   #example input
    project1 = Project.objects.create(
        title='Project 1',
        completion='2024-01-01',
        is_published=True,
        photo_main=image_file  
    )
    project2 = Project.objects.create(
        title='Project 2',
        completion='2023-01-01',
        is_published=True,
        photo_main=image_file
    )
    project3 = Project.objects.create(
        title='Project 3',
        completion='2022-01-01',
        is_published=True,
        photo_main=image_file
    )
    project4 = Project.objects.create(
        title='Project 4',
        completion='2025-01-01',
        is_published=False,
        photo_main=image_file
    )

    client = Client()

    response = client.get(reverse('index'))

    assert response.status_code == 200

    assert 'pages/index.html' in [t.name for t in response.templates]

    context_projects = response.context['projects']

    assert len(context_projects) == 3

    assert context_projects[0] == project1  
    assert context_projects[1] == project2 
    assert context_projects[2] == project3  

    assert all(project.is_published for project in context_projects)
