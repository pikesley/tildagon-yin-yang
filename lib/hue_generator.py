def hues(count, offset=0):
    """Generate sets of hues."""
    h = {"top": [(((i + 1) / count) + offset) % 1 for i in range(count)]}
    h["bottom"] = list(reversed(h["top"]))

    return h
