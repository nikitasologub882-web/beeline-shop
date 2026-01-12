# import random
#
# my_list = ['text', 'one', 'two']
# print(random.choice(my_list))

import pytest

@pytest.fixture()
def before_after():
    print("before test")
    yield
    print("\nafter test")


def test_demo1():
    assert 1 == 1

def test_demo2(before_after):
    assert 2 == 2
