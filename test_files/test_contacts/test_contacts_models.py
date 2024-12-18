import pytest
from datetime import datetime
from contacts.models import Contact  # Replace 'myapp' with the actual app name

@pytest.mark.django_db
def test_contact_model():
   #example data input
    contact1 = Contact.objects.create(
        name="John Doe",
        email="johndoe@example.com",
        phone="1234567890",
        subject="Test Subject",
        message="This is a test message."
    )

    contact_from_db = Contact.objects.get(id=contact1.id)

    assert contact_from_db.name == "John Doe", "Name should match the created instance"
    assert contact_from_db.email == "johndoe@example.com", "Email should match the created instance"
