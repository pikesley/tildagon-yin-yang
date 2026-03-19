def centres(slices, full_diameter=240):
    """Find centres."""
    full_radius = full_diameter / 2
    step = round(full_radius / slices)
    return [0 - (step * i) for i in range(slices)]


def radii(slices, full_diameter=240):
    """Find diameters."""
    step = full_diameter / (2 * slices)
    return reversed([round(step * (i + 1)) for i in range(slices)])


def circles(slices, full_diameter=240):
    """Find circles."""
    return zip(  # noqa: B905
        centres(slices, full_diameter=full_diameter),
        radii(slices, full_diameter=full_diameter),
    )
