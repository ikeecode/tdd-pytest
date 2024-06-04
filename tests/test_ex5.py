import pytest 

def test_review(review_factory):
    review = review_factory.build()
    print(review_factory.content)
    assert True


def test_comment(comment_factory):
    comment = comment_factory.build()
    print(comment.content)
    assert True 