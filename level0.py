def level0(area):
    panels = []

    while area > 0:
        largest = int(area**0.5)**2
        panels.append(largest)
        area -= largest

    return panels
