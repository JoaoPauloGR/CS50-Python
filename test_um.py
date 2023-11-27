from um import count

def test_count():
    assert count("hello, um, world") == 1
    assert count("hello, um, world, um") == 2
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count ("Um? Mum?") == 1