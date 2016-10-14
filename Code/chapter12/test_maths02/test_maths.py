def test_add():
    if not 1+1 == 2:
        raise AssertionError()

def test_subtract():
    a = 1
    b = a + 1
    c = b-1
    assert b-a == c
