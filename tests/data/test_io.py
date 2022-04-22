from green_node.data.io import get_example, get_root


def test_get_root():
    assert get_root()


def test_get_example():
    assert get_example("shortest-path.xml").exists()
