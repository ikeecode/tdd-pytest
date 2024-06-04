import pytest 

from pytest_factoryboy import register
from tests.factories import UserFactory, ReviewFactory, CommentFactory

register(UserFactory)
register(ReviewFactory)
register(CommentFactory)


@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user 