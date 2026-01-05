def centres(slices, full_diameter=240):
    """Find centres."""
    full_radius = full_diameter / 2

    step = round(full_radius / slices)
    c = [step * i for i in range(slices)]
    c = [0 - i for i in reversed(c)][:-1] + c

    return c  # noqa: RET504


def radii(slices, full_diameter=240):
    """Find diameters."""
    step = full_diameter / (2 * slices)
    r = [round(step * (i + 1)) for i in range(slices)]
    r.extend(list(reversed(r))[1:])

    return r


def circles(slices, full_diameter=240):
    """Find circles."""
    return zip(  # noqa: B905
        centres(slices, full_diameter=full_diameter),
        radii(slices, full_diameter=full_diameter),
    )
