import pytest



def test_new_user(user_factory):
    print(user_factory.username)
    assert True 


def test_menu_user1(new_user1):
    print(new_user1.username)
    assert True 

