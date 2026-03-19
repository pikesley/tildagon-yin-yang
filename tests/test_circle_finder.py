from lib.circle_finder import centres, circles, radii


def test_centres():
    """Test."""
    assert list(centres(2)) == [0, -60]
    assert list(centres(3)) == [0, -40, -80]


def test_radii():
    """Test."""
    assert list(radii(2)) == [120, 60]
    assert list(radii(3)) == [120, 80, 40]


def test_circles():
    """Test."""
    assert list(circles(2)) == [
        (0, 120),
        (-60, 60),
    ]

    assert list(circles(3)) == [
        (0, 120),
        (-40, 80),
        (-80, 40),
    ]
