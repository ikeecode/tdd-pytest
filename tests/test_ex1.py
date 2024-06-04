import pytest 


@pytest.mark.slow
def sayHello():
    assert 'hello' == 'hello'

def test_example():
    assert 1 == 1

