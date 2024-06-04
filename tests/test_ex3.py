import pytest

from django.contrib.auth.models import User 


@pytest.fixture
def user_1(db):
    return User.objects.create(username="user1")


@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password('brasko')

    assert user_1.check_password("brasko") is True

