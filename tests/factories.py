import factory
from faker import Faker 

from django.contrib.auth.models import User 

from app1.models import Review, Comment

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User 

    username = fake.name 
    is_staff = 'True'



class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review
    
    content = fake.text()
    user    = factory.SubFactory(UserFactory)




class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment 
    
    user    = factory.SubFactory(UserFactory)
    review  = factory.SubFactory(ReviewFactory)
    content = fake.text()
