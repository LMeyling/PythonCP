# Status: not in use
def cross(point_a, point_b, point_c):
    vec_ab = ((point_b[0] - point_a[0]), (point_b[1] - point_a[1]))
    vec_ac = ((point_c[0] - point_b[0]), (point_c[1] - point_b[1]))
    return (vec_ab[0] * vec_ac[1]) - (vec_ab[1] * vec_ac[0])


def form_lower_hull(all_points):
    # Punkte werden erst nach x, dann nach y sortiert
    all_points = sorted(all_points, key=lambda element: (element[0], element[1]))
    sol = []
    for c in all_points:
        # Nächster Punkt wird dem Solution Array angehangen
        sol.append(c)
        # Immer wenn es mindestens 3 Punkte im Solution Array gibt, überprüfe die letzten 3
        while len(sol) > 2 and cross(sol[-3], sol[-2], sol[-1]) <= 0:
            # Falls die Richtung mit dem Uhrzeigersinn geht, dann muss der vorletzte Punkt raus
            sol.pop(-2)
    return sol


def form_upper_hull(all_points):
    # Punkte werden absteigend nach x und dann y Wert sortiert
    all_points = sorted(all_points, key=lambda element: (-element[0], -element[1]))
    sol = []
    for c in all_points:
        # Punkt wird dem Solution Array angehangen
        sol.append(c)
        # Immer wenn es mindestens 3 Punkte im Solution Array gibt, überprüfe die letzten 3 Punkte
        while len(sol) > 2 and cross(sol[-3], sol[-2], sol[-1]) <= 0:
            # Falls die Richtung mit dem Uhrzeigersinn geht, dann muss der vorletzte Punkt raus
            sol.pop(-2)
    sol.reverse()
    return sol