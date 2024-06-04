import pytest 

@pytest.fixture(scope="session")
def fixture_1():
    print('running fixuture 1')

    return 1 


def test_example2(fixture_1):
    num = fixture_1

    assert num == 1

def test_example3(fixture_1):
    num = fixture_1

    assert num == 1



