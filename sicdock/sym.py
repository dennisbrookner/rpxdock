from homog import hnormalized
import numpy as np


tetrahedral_axes = {
    2: hnormalized([1, 0, 0]),
    3: hnormalized([1, 1, 1]),
    33: hnormalized([1, 1, -1]),
}  # other c3
octahedral_axes = {
    2: hnormalized([1, 1, 0]),
    3: hnormalized([1, 1, 1]),
    4: hnormalized([1, 0, 0]),
}
icosahedral_axes = {
    2: hnormalized([1, 0, 0]),
    3: hnormalized([0.934172, 0.000000, 0.356822]),
    5: hnormalized([0.850651, 0.525731, 0.000000]),
}

tetrahedral_second_axes = {
    2: hnormalized([0, 1, 0]),
    3: hnormalized([1, -1, -1]),
    7: hnormalized([-1, -1, -1]),
}  # other c3
octahedral_second_axes = {
    2: hnormalized([1, -1, 0]),
    3: hnormalized([1, -1, 1]),
    4: hnormalized([0, 1, 0]),
}
icosahedral_second_axes = {
    2: hnormalized([0.809017, 0.309017, -0.5]),
    3: hnormalized([0.934172372, 0, -0.356822067]),
    5: hnormalized([0.850651, -0.525731, 0.000000]),
}
symaxes_second = dict(
    T=tetrahedral_second_axes, O=octahedral_second_axes, I=icosahedral_second_axes
)


tetrahedral_frames = np.array(
    [
        (
            (+1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, +1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, -1.000000, +0.000000, +0.000000),
            (+0.000000, -0.000000, -1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +1.000000, -0.000000, +0.000000),
            (-0.000000, +0.000000, +1.000000, +0.000000),
            (+1.000000, -0.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -1.000000, +0.000000, +0.000000),
            (-0.000000, -0.000000, -1.000000, +0.000000),
            (+1.000000, +0.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +1.000000, -0.000000, +0.000000),
            (+0.000000, -0.000000, -1.000000, +0.000000),
            (-1.000000, +0.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.000000, +0.000000, +1.000000, +0.000000),
            (+1.000000, -0.000000, +0.000000, +0.000000),
            (+0.000000, +1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +1.000000, +0.000000),
            (-1.000000, -0.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.000000, -0.000000, -1.000000, +0.000000),
            (+1.000000, +0.000000, -0.000000, +0.000000),
            (+0.000000, -1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -0.000000, -1.000000, +0.000000),
            (-1.000000, -0.000000, -0.000000, +0.000000),
            (-0.000000, +1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.000000, +0.000000, +1.000000, +0.000000),
            (-1.000000, +0.000000, -0.000000, +0.000000),
            (-0.000000, -1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-1.000000, -0.000000, -0.000000, +0.000000),
            (-0.000000, +1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, -1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-1.000000, +0.000000, -0.000000, +0.000000),
            (-0.000000, -1.000000, +0.000000, +0.000000),
            (-0.000000, +0.000000, +1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
    ]
)

octahedral_frames = np.array(
    [
        (
            (+1.000000, +0.000000, -0.000000, +0.000000),
            (+0.000000, +1.000000, +0.000000, +0.000000),
            (+0.000000, -0.000000, +1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +1.000000, +0.000000, +0.000000),
            (+1.000000, +0.000000, -0.000000, +0.000000),
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -0.000000, +1.000000, +0.000000),
            (+1.000000, +0.000000, -0.000000, +0.000000),
            (-0.000000, +1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+1.000000, +0.000000, -0.000000, +0.000000),
            (+0.000000, -0.000000, +1.000000, +0.000000),
            (+0.000000, -1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (+0.000000, +1.000000, +0.000000, +0.000000),
            (+1.000000, -0.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.000000, +1.000000, +0.000000, +0.000000),
            (+0.000000, -0.000000, +1.000000, +0.000000),
            (+1.000000, +0.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +1.000000, +0.000000, +0.000000),
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (-1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -0.000000, +1.000000, +0.000000),
            (-0.000000, +1.000000, +0.000000, +0.000000),
            (-1.000000, -0.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -1.000000, -0.000000, +0.000000),
            (+1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, -0.000000, +1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+1.000000, -0.000000, -0.000000, +0.000000),
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (+0.000000, +1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, -1.000000, -0.000000, +0.000000),
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (+1.000000, -0.000000, -0.000000, +0.000000),
            (-0.000000, -1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, +1.000000, -0.000000, +0.000000),
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-1.000000, -0.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +1.000000, +0.000000),
            (-0.000000, +1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -0.000000, +1.000000, +0.000000),
            (+0.000000, -1.000000, -0.000000, +0.000000),
            (+1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +1.000000, -0.000000, +0.000000),
            (-1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, -0.000000, +1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +0.000000, +1.000000, +0.000000),
            (-1.000000, -0.000000, +0.000000, +0.000000),
            (+0.000000, -1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -1.000000, -0.000000, +0.000000),
            (-0.000000, -0.000000, +1.000000, +0.000000),
            (-1.000000, -0.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.000000, -1.000000, -0.000000, +0.000000),
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (+1.000000, -0.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (-1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, +1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +0.000000, -1.000000, +0.000000),
            (-0.000000, -1.000000, -0.000000, +0.000000),
            (-1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-1.000000, +0.000000, +0.000000, +0.000000),
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (-0.000000, -1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-1.000000, -0.000000, -0.000000, +0.000000),
            (+0.000000, -1.000000, -0.000000, +0.000000),
            (-0.000000, -0.000000, +1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -1.000000, -0.000000, +0.000000),
            (-1.000000, -0.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, -1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
    ]
)

icosahedral_frames = np.array(
    [
        (
            (+1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, +1.000000, +0.000000, +0.000000),
            (+0.000000, -0.000000, +1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.809017, +0.309017, +0.500000, +0.000000),
            (+0.309017, +0.500000, -0.809017, +0.000000),
            (-0.500000, +0.809017, +0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, -1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, -1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.809017, +0.309017, +0.500000, +0.000000),
            (-0.309017, -0.500000, +0.809017, +0.000000),
            (+0.500000, -0.809017, -0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.809017, +0.309017, -0.500000, +0.000000),
            (+0.309017, +0.500000, +0.809017, +0.000000),
            (+0.500000, -0.809017, +0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.809017, +0.309017, -0.500000, +0.000000),
            (-0.309017, -0.500000, -0.809017, +0.000000),
            (-0.500000, +0.809017, -0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.809017, -0.309017, +0.500000, +0.000000),
            (+0.309017, -0.500000, -0.809017, +0.000000),
            (+0.500000, +0.809017, -0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.809017, -0.309017, +0.500000, +0.000000),
            (-0.309017, +0.500000, +0.809017, +0.000000),
            (-0.500000, -0.809017, +0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.809017, -0.309017, -0.500000, +0.000000),
            (+0.309017, -0.500000, +0.809017, +0.000000),
            (-0.500000, -0.809017, -0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.809017, -0.309017, -0.500000, +0.000000),
            (-0.309017, +0.500000, -0.809017, +0.000000),
            (+0.500000, +0.809017, +0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.500000, +0.809017, +0.309017, +0.000000),
            (+0.809017, -0.309017, -0.500000, +0.000000),
            (-0.309017, +0.500000, -0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.500000, +0.809017, +0.309017, +0.000000),
            (-0.809017, +0.309017, +0.500000, +0.000000),
            (+0.309017, -0.500000, +0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.500000, +0.809017, -0.309017, +0.000000),
            (+0.809017, -0.309017, +0.500000, +0.000000),
            (+0.309017, -0.500000, -0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.500000, +0.809017, -0.309017, +0.000000),
            (-0.809017, +0.309017, -0.500000, +0.000000),
            (-0.309017, +0.500000, +0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.500000, -0.809017, +0.309017, +0.000000),
            (+0.809017, +0.309017, -0.500000, +0.000000),
            (+0.309017, +0.500000, +0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.500000, -0.809017, +0.309017, +0.000000),
            (-0.809017, -0.309017, +0.500000, +0.000000),
            (-0.309017, -0.500000, -0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.500000, -0.809017, -0.309017, +0.000000),
            (+0.809017, +0.309017, +0.500000, +0.000000),
            (-0.309017, -0.500000, +0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.500000, -0.809017, -0.309017, +0.000000),
            (-0.809017, -0.309017, -0.500000, +0.000000),
            (+0.309017, +0.500000, -0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.309017, +0.500000, +0.809017, +0.000000),
            (+0.500000, -0.809017, +0.309017, +0.000000),
            (+0.809017, +0.309017, -0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.309017, +0.500000, +0.809017, +0.000000),
            (-0.500000, +0.809017, -0.309017, +0.000000),
            (-0.809017, -0.309017, +0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.309017, +0.500000, -0.809017, +0.000000),
            (+0.500000, -0.809017, -0.309017, +0.000000),
            (-0.809017, -0.309017, -0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.309017, +0.500000, -0.809017, +0.000000),
            (-0.500000, +0.809017, +0.309017, +0.000000),
            (+0.809017, +0.309017, +0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.309017, -0.500000, +0.809017, +0.000000),
            (+0.500000, +0.809017, +0.309017, +0.000000),
            (-0.809017, +0.309017, +0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.309017, -0.500000, +0.809017, +0.000000),
            (-0.500000, -0.809017, -0.309017, +0.000000),
            (+0.809017, -0.309017, -0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.309017, -0.500000, -0.809017, +0.000000),
            (+0.500000, +0.809017, -0.309017, +0.000000),
            (+0.809017, -0.309017, +0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.309017, -0.500000, -0.809017, +0.000000),
            (-0.500000, -0.809017, +0.309017, +0.000000),
            (-0.809017, +0.309017, -0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +1.000000, +0.000000, +0.000000),
            (+0.000000, -0.000000, +1.000000, +0.000000),
            (+1.000000, -0.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +1.000000, +0.000000, +0.000000),
            (-0.000000, +0.000000, -1.000000, +0.000000),
            (-1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +0.000000, +1.000000, +0.000000),
            (+1.000000, -0.000000, -0.000000, +0.000000),
            (+0.000000, +1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, +0.000000, +1.000000, +0.000000),
            (-1.000000, +0.000000, +0.000000, +0.000000),
            (-0.000000, -1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +1.000000, +0.000000),
            (-1.000000, -0.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -1.000000, +0.000000, +0.000000),
            (-0.000000, -0.000000, -1.000000, +0.000000),
            (+1.000000, +0.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -0.000000, -1.000000, +0.000000),
            (+1.000000, +0.000000, +0.000000, +0.000000),
            (+0.000000, -1.000000, +0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (+0.000000, -0.000000, -1.000000, +0.000000),
            (-1.000000, -0.000000, -0.000000, +0.000000),
            (-0.000000, +1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-1.000000, -0.000000, +0.000000, +0.000000),
            (+0.000000, -1.000000, -0.000000, +0.000000),
            (+0.000000, +0.000000, +1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-1.000000, -0.000000, +0.000000, +0.000000),
            (-0.000000, +1.000000, +0.000000, +0.000000),
            (-0.000000, -0.000000, -1.000000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.809017, +0.309017, +0.500000, +0.000000),
            (+0.309017, -0.500000, +0.809017, +0.000000),
            (+0.500000, +0.809017, +0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.809017, +0.309017, +0.500000, +0.000000),
            (-0.309017, +0.500000, -0.809017, +0.000000),
            (-0.500000, -0.809017, -0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.809017, +0.309017, -0.500000, +0.000000),
            (+0.309017, -0.500000, -0.809017, +0.000000),
            (-0.500000, -0.809017, +0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.809017, +0.309017, -0.500000, +0.000000),
            (-0.309017, +0.500000, +0.809017, +0.000000),
            (+0.500000, +0.809017, -0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.809017, -0.309017, +0.500000, +0.000000),
            (+0.309017, +0.500000, +0.809017, +0.000000),
            (-0.500000, +0.809017, -0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.809017, -0.309017, +0.500000, +0.000000),
            (-0.309017, -0.500000, -0.809017, +0.000000),
            (+0.500000, -0.809017, +0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.809017, -0.309017, -0.500000, +0.000000),
            (+0.309017, +0.500000, -0.809017, +0.000000),
            (+0.500000, -0.809017, -0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.809017, -0.309017, -0.500000, +0.000000),
            (-0.309017, -0.500000, +0.809017, +0.000000),
            (-0.500000, +0.809017, +0.309017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.500000, +0.809017, +0.309017, +0.000000),
            (+0.809017, +0.309017, +0.500000, +0.000000),
            (+0.309017, +0.500000, -0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.500000, +0.809017, +0.309017, +0.000000),
            (-0.809017, -0.309017, -0.500000, +0.000000),
            (-0.309017, -0.500000, +0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.500000, +0.809017, -0.309017, +0.000000),
            (+0.809017, +0.309017, -0.500000, +0.000000),
            (-0.309017, -0.500000, -0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.500000, +0.809017, -0.309017, +0.000000),
            (-0.809017, -0.309017, +0.500000, +0.000000),
            (+0.309017, +0.500000, +0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.500000, -0.809017, +0.309017, +0.000000),
            (+0.809017, -0.309017, +0.500000, +0.000000),
            (-0.309017, +0.500000, +0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.500000, -0.809017, +0.309017, +0.000000),
            (-0.809017, +0.309017, -0.500000, +0.000000),
            (+0.309017, -0.500000, -0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.500000, -0.809017, -0.309017, +0.000000),
            (+0.809017, -0.309017, -0.500000, +0.000000),
            (+0.309017, -0.500000, +0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.500000, -0.809017, -0.309017, +0.000000),
            (-0.809017, +0.309017, +0.500000, +0.000000),
            (-0.309017, +0.500000, -0.809017, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.309017, +0.500000, +0.809017, +0.000000),
            (+0.500000, +0.809017, -0.309017, +0.000000),
            (-0.809017, +0.309017, -0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.309017, +0.500000, +0.809017, +0.000000),
            (-0.500000, -0.809017, +0.309017, +0.000000),
            (+0.809017, -0.309017, +0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.309017, +0.500000, -0.809017, +0.000000),
            (+0.500000, +0.809017, +0.309017, +0.000000),
            (+0.809017, -0.309017, -0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.309017, +0.500000, -0.809017, +0.000000),
            (-0.500000, -0.809017, -0.309017, +0.000000),
            (-0.809017, +0.309017, +0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.309017, -0.500000, +0.809017, +0.000000),
            (+0.500000, -0.809017, -0.309017, +0.000000),
            (+0.809017, +0.309017, +0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.309017, -0.500000, +0.809017, +0.000000),
            (-0.500000, +0.809017, +0.309017, +0.000000),
            (-0.809017, -0.309017, -0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.309017, -0.500000, -0.809017, +0.000000),
            (+0.500000, -0.809017, +0.309017, +0.000000),
            (-0.809017, -0.309017, +0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
        (
            (-0.309017, -0.500000, -0.809017, +0.000000),
            (-0.500000, +0.809017, -0.309017, +0.000000),
            (+0.809017, +0.309017, -0.500000, +0.000000),
            (+0.000000, +0.000000, +0.000000, +1.000000),
        ),
    ]
)


symframes = dict(T=tetrahedral_frames, O=octahedral_frames, I=icosahedral_frames)
symaxes = dict(T=tetrahedral_axes, O=octahedral_axes, I=icosahedral_axes)


sym_to_neighbor_olig = dict(
    T={2: symframes["T"][2], 3: symframes["T"][1], 33: symframes["T"][1]},
    O={2: symframes["O"][2], 3: symframes["O"][1], 4: symframes["O"][1]},
    I={2: symframes["I"][1], 3: symframes["I"][1], 5: symframes["I"][2]},
)
