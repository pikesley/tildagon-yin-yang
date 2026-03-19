from lib.hue_generator import hues


def test_hue_generator():
    """Test."""
    assert hues(3) == {
        "top": [1 / 3, 2 / 3, 0],
        "bottom": [0, 2 / 3, 1 / 3],
    }
    assert hues(4) == {
        "top": [0.25, 0.5, 0.75, 0],
        "bottom": [0, 0.75, 0.5, 0.25],
    }


def test_with_offset():
    """Test."""
    assert hues(4, 0.5) == {
        "bottom": [0.5, 0.25, 0.0, 0.75],
        "top": [0.75, 0.0, 0.25, 0.5],
    }
