import pytest

class C:
    def f(self):
        return 1

    def g(self):
        return 2

@pytest.fixture

def test_f():
    c = C()
    assert c.f() == 1


def test_g():
    c = C()
    assert c.g() == 2