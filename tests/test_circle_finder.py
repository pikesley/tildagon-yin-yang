from lib.circle_finder import centres, circles, radii


def test_centres():
    """Test."""
    assert centres(2) == [-60, 0, 60]
    assert centres(3) == [-80, -40, 0, 40, 80]
    # assert centres(4) == [-90, -30, 30, 90]


def test_radii():
    """Test."""
    assert radii(2) == [60, 120, 60]
    assert radii(3) == [40, 80, 120, 80, 40]


def test_circles():
    """Test."""
    assert list(circles(2)) == [
        (-60, 60),
        (0, 120),
        (60, 60),
    ]

    assert list(circles(3)) == [
        (-80, 40),
        (-40, 80),
        (0, 120),
        (40, 80),
        (80, 40),
    ]
