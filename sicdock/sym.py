from homog import hnormalized
import numpy as np

tetrahedral_frames = np.load("sicdock/data/tetrahedral_frames.pickle")
octahedral_frames = np.load("sicdock/data/octahedral_frames.pickle")
icosahedral_frames = np.load("sicdock/data/icosahedral_frames.pickle")

frames = dict(T=tetrahedral_frames, O=octahedral_frames, I=icosahedral_frames)


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
axes = dict(T=tetrahedral_axes, O=octahedral_axes, I=icosahedral_axes)


to_neighbor_olig = dict(
    T={2: frames["T"][2], 3: frames["T"][1], 33: frames["T"][1]},
    O={2: frames["O"][2], 3: frames["O"][1], 4: frames["O"][1]},
    I={2: frames["I"][1], 3: frames["I"][1], 5: frames["I"][2]},
)

axes_second = {
    s: {k: to_neighbor_olig[s][k] @ v for k, v in axes[s].items()} for s in "TOI"
}


# tetrahedral_frames = np.array(
# [
# (
# (+1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, +1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, -1.000000, +0.000000, +0.000000),
# (+0.000000, -0.000000, -1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +1.000000, -0.000000, +0.000000),
# (-0.000000, +0.000000, +1.000000, +0.000000),
# (+1.000000, -0.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -1.000000, +0.000000, +0.000000),
# (-0.000000, -0.000000, -1.000000, +0.000000),
# (+1.000000, +0.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +1.000000, -0.000000, +0.000000),
# (+0.000000, -0.000000, -1.000000, +0.000000),
# (-1.000000, +0.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.000000, +0.000000, +1.000000, +0.000000),
# (+1.000000, -0.000000, +0.000000, +0.000000),
# (+0.000000, +1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +1.000000, +0.000000),
# (-1.000000, -0.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.000000, -0.000000, -1.000000, +0.000000),
# (+1.000000, +0.000000, -0.000000, +0.000000),
# (+0.000000, -1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -0.000000, -1.000000, +0.000000),
# (-1.000000, -0.000000, -0.000000, +0.000000),
# (-0.000000, +1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.000000, +0.000000, +1.000000, +0.000000),
# (-1.000000, +0.000000, -0.000000, +0.000000),
# (-0.000000, -1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-1.000000, -0.000000, -0.000000, +0.000000),
# (-0.000000, +1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, -1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-1.000000, +0.000000, -0.000000, +0.000000),
# (-0.000000, -1.000000, +0.000000, +0.000000),
# (-0.000000, +0.000000, +1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# ]
# )
#
# octahedral_frames = np.array(
# [
# (
# (+1.000000, +0.000000, -0.000000, +0.000000),
# (+0.000000, +1.000000, +0.000000, +0.000000),
# (+0.000000, -0.000000, +1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +1.000000, +0.000000, +0.000000),
# (+1.000000, +0.000000, -0.000000, +0.000000),
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -0.000000, +1.000000, +0.000000),
# (+1.000000, +0.000000, -0.000000, +0.000000),
# (-0.000000, +1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+1.000000, +0.000000, -0.000000, +0.000000),
# (+0.000000, -0.000000, +1.000000, +0.000000),
# (+0.000000, -1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (+0.000000, +1.000000, +0.000000, +0.000000),
# (+1.000000, -0.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.000000, +1.000000, +0.000000, +0.000000),
# (+0.000000, -0.000000, +1.000000, +0.000000),
# (+1.000000, +0.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +1.000000, +0.000000, +0.000000),
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (-1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -0.000000, +1.000000, +0.000000),
# (-0.000000, +1.000000, +0.000000, +0.000000),
# (-1.000000, -0.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -1.000000, -0.000000, +0.000000),
# (+1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, -0.000000, +1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+1.000000, -0.000000, -0.000000, +0.000000),
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (+0.000000, +1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, -1.000000, -0.000000, +0.000000),
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (+1.000000, -0.000000, -0.000000, +0.000000),
# (-0.000000, -1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, +1.000000, -0.000000, +0.000000),
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-1.000000, -0.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +1.000000, +0.000000),
# (-0.000000, +1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -0.000000, +1.000000, +0.000000),
# (+0.000000, -1.000000, -0.000000, +0.000000),
# (+1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +1.000000, -0.000000, +0.000000),
# (-1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, -0.000000, +1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +0.000000, +1.000000, +0.000000),
# (-1.000000, -0.000000, +0.000000, +0.000000),
# (+0.000000, -1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -1.000000, -0.000000, +0.000000),
# (-0.000000, -0.000000, +1.000000, +0.000000),
# (-1.000000, -0.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.000000, -1.000000, -0.000000, +0.000000),
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (+1.000000, -0.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (-1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, +1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +0.000000, -1.000000, +0.000000),
# (-0.000000, -1.000000, -0.000000, +0.000000),
# (-1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-1.000000, +0.000000, +0.000000, +0.000000),
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (-0.000000, -1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-1.000000, -0.000000, -0.000000, +0.000000),
# (+0.000000, -1.000000, -0.000000, +0.000000),
# (-0.000000, -0.000000, +1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -1.000000, -0.000000, +0.000000),
# (-1.000000, -0.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, -1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# ]
# )
#
# icosahedral_frames = np.array(
# [
# (
# (+1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, +1.000000, +0.000000, +0.000000),
# (+0.000000, -0.000000, +1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.809017, +0.309017, +0.500000, +0.000000),
# (+0.309017, +0.500000, -0.809017, +0.000000),
# (-0.500000, +0.809017, +0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, -1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, -1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.809017, +0.309017, +0.500000, +0.000000),
# (-0.309017, -0.500000, +0.809017, +0.000000),
# (+0.500000, -0.809017, -0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.809017, +0.309017, -0.500000, +0.000000),
# (+0.309017, +0.500000, +0.809017, +0.000000),
# (+0.500000, -0.809017, +0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.809017, +0.309017, -0.500000, +0.000000),
# (-0.309017, -0.500000, -0.809017, +0.000000),
# (-0.500000, +0.809017, -0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.809017, -0.309017, +0.500000, +0.000000),
# (+0.309017, -0.500000, -0.809017, +0.000000),
# (+0.500000, +0.809017, -0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.809017, -0.309017, +0.500000, +0.000000),
# (-0.309017, +0.500000, +0.809017, +0.000000),
# (-0.500000, -0.809017, +0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.809017, -0.309017, -0.500000, +0.000000),
# (+0.309017, -0.500000, +0.809017, +0.000000),
# (-0.500000, -0.809017, -0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.809017, -0.309017, -0.500000, +0.000000),
# (-0.309017, +0.500000, -0.809017, +0.000000),
# (+0.500000, +0.809017, +0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.500000, +0.809017, +0.309017, +0.000000),
# (+0.809017, -0.309017, -0.500000, +0.000000),
# (-0.309017, +0.500000, -0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.500000, +0.809017, +0.309017, +0.000000),
# (-0.809017, +0.309017, +0.500000, +0.000000),
# (+0.309017, -0.500000, +0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.500000, +0.809017, -0.309017, +0.000000),
# (+0.809017, -0.309017, +0.500000, +0.000000),
# (+0.309017, -0.500000, -0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.500000, +0.809017, -0.309017, +0.000000),
# (-0.809017, +0.309017, -0.500000, +0.000000),
# (-0.309017, +0.500000, +0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.500000, -0.809017, +0.309017, +0.000000),
# (+0.809017, +0.309017, -0.500000, +0.000000),
# (+0.309017, +0.500000, +0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.500000, -0.809017, +0.309017, +0.000000),
# (-0.809017, -0.309017, +0.500000, +0.000000),
# (-0.309017, -0.500000, -0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.500000, -0.809017, -0.309017, +0.000000),
# (+0.809017, +0.309017, +0.500000, +0.000000),
# (-0.309017, -0.500000, +0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.500000, -0.809017, -0.309017, +0.000000),
# (-0.809017, -0.309017, -0.500000, +0.000000),
# (+0.309017, +0.500000, -0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.309017, +0.500000, +0.809017, +0.000000),
# (+0.500000, -0.809017, +0.309017, +0.000000),
# (+0.809017, +0.309017, -0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.309017, +0.500000, +0.809017, +0.000000),
# (-0.500000, +0.809017, -0.309017, +0.000000),
# (-0.809017, -0.309017, +0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.309017, +0.500000, -0.809017, +0.000000),
# (+0.500000, -0.809017, -0.309017, +0.000000),
# (-0.809017, -0.309017, -0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.309017, +0.500000, -0.809017, +0.000000),
# (-0.500000, +0.809017, +0.309017, +0.000000),
# (+0.809017, +0.309017, +0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.309017, -0.500000, +0.809017, +0.000000),
# (+0.500000, +0.809017, +0.309017, +0.000000),
# (-0.809017, +0.309017, +0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.309017, -0.500000, +0.809017, +0.000000),
# (-0.500000, -0.809017, -0.309017, +0.000000),
# (+0.809017, -0.309017, -0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.309017, -0.500000, -0.809017, +0.000000),
# (+0.500000, +0.809017, -0.309017, +0.000000),
# (+0.809017, -0.309017, +0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.309017, -0.500000, -0.809017, +0.000000),
# (-0.500000, -0.809017, +0.309017, +0.000000),
# (-0.809017, +0.309017, -0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +1.000000, +0.000000, +0.000000),
# (+0.000000, -0.000000, +1.000000, +0.000000),
# (+1.000000, -0.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +1.000000, +0.000000, +0.000000),
# (-0.000000, +0.000000, -1.000000, +0.000000),
# (-1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +0.000000, +1.000000, +0.000000),
# (+1.000000, -0.000000, -0.000000, +0.000000),
# (+0.000000, +1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, +0.000000, +1.000000, +0.000000),
# (-1.000000, +0.000000, +0.000000, +0.000000),
# (-0.000000, -1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +1.000000, +0.000000),
# (-1.000000, -0.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -1.000000, +0.000000, +0.000000),
# (-0.000000, -0.000000, -1.000000, +0.000000),
# (+1.000000, +0.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -0.000000, -1.000000, +0.000000),
# (+1.000000, +0.000000, +0.000000, +0.000000),
# (+0.000000, -1.000000, +0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (+0.000000, -0.000000, -1.000000, +0.000000),
# (-1.000000, -0.000000, -0.000000, +0.000000),
# (-0.000000, +1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-1.000000, -0.000000, +0.000000, +0.000000),
# (+0.000000, -1.000000, -0.000000, +0.000000),
# (+0.000000, +0.000000, +1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-1.000000, -0.000000, +0.000000, +0.000000),
# (-0.000000, +1.000000, +0.000000, +0.000000),
# (-0.000000, -0.000000, -1.000000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.809017, +0.309017, +0.500000, +0.000000),
# (+0.309017, -0.500000, +0.809017, +0.000000),
# (+0.500000, +0.809017, +0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.809017, +0.309017, +0.500000, +0.000000),
# (-0.309017, +0.500000, -0.809017, +0.000000),
# (-0.500000, -0.809017, -0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.809017, +0.309017, -0.500000, +0.000000),
# (+0.309017, -0.500000, -0.809017, +0.000000),
# (-0.500000, -0.809017, +0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.809017, +0.309017, -0.500000, +0.000000),
# (-0.309017, +0.500000, +0.809017, +0.000000),
# (+0.500000, +0.809017, -0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.809017, -0.309017, +0.500000, +0.000000),
# (+0.309017, +0.500000, +0.809017, +0.000000),
# (-0.500000, +0.809017, -0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.809017, -0.309017, +0.500000, +0.000000),
# (-0.309017, -0.500000, -0.809017, +0.000000),
# (+0.500000, -0.809017, +0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.809017, -0.309017, -0.500000, +0.000000),
# (+0.309017, +0.500000, -0.809017, +0.000000),
# (+0.500000, -0.809017, -0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.809017, -0.309017, -0.500000, +0.000000),
# (-0.309017, -0.500000, +0.809017, +0.000000),
# (-0.500000, +0.809017, +0.309017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.500000, +0.809017, +0.309017, +0.000000),
# (+0.809017, +0.309017, +0.500000, +0.000000),
# (+0.309017, +0.500000, -0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.500000, +0.809017, +0.309017, +0.000000),
# (-0.809017, -0.309017, -0.500000, +0.000000),
# (-0.309017, -0.500000, +0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.500000, +0.809017, -0.309017, +0.000000),
# (+0.809017, +0.309017, -0.500000, +0.000000),
# (-0.309017, -0.500000, -0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.500000, +0.809017, -0.309017, +0.000000),
# (-0.809017, -0.309017, +0.500000, +0.000000),
# (+0.309017, +0.500000, +0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.500000, -0.809017, +0.309017, +0.000000),
# (+0.809017, -0.309017, +0.500000, +0.000000),
# (-0.309017, +0.500000, +0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.500000, -0.809017, +0.309017, +0.000000),
# (-0.809017, +0.309017, -0.500000, +0.000000),
# (+0.309017, -0.500000, -0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.500000, -0.809017, -0.309017, +0.000000),
# (+0.809017, -0.309017, -0.500000, +0.000000),
# (+0.309017, -0.500000, +0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.500000, -0.809017, -0.309017, +0.000000),
# (-0.809017, +0.309017, +0.500000, +0.000000),
# (-0.309017, +0.500000, -0.809017, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.309017, +0.500000, +0.809017, +0.000000),
# (+0.500000, +0.809017, -0.309017, +0.000000),
# (-0.809017, +0.309017, -0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.309017, +0.500000, +0.809017, +0.000000),
# (-0.500000, -0.809017, +0.309017, +0.000000),
# (+0.809017, -0.309017, +0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.309017, +0.500000, -0.809017, +0.000000),
# (+0.500000, +0.809017, +0.309017, +0.000000),
# (+0.809017, -0.309017, -0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.309017, +0.500000, -0.809017, +0.000000),
# (-0.500000, -0.809017, -0.309017, +0.000000),
# (-0.809017, +0.309017, +0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.309017, -0.500000, +0.809017, +0.000000),
# (+0.500000, -0.809017, -0.309017, +0.000000),
# (+0.809017, +0.309017, +0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.309017, -0.500000, +0.809017, +0.000000),
# (-0.500000, +0.809017, +0.309017, +0.000000),
# (-0.809017, -0.309017, -0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.309017, -0.500000, -0.809017, +0.000000),
# (+0.500000, -0.809017, +0.309017, +0.000000),
# (-0.809017, -0.309017, +0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# (
# (-0.309017, -0.500000, -0.809017, +0.000000),
# (-0.500000, +0.809017, -0.309017, +0.000000),
# (+0.809017, +0.309017, -0.500000, +0.000000),
# (+0.000000, +0.000000, +0.000000, +1.000000),
# ),
# ]
# )
#
# tetrahedral_frames.dump("sicdock/data/tetrahedral_frames.pickle")
# octahedral_frames.dump("sicdock/data/octahedral_frames.pickle")
# icosahedral_frames.dump("sicdock/data/icosahedral_frames.pickle")
