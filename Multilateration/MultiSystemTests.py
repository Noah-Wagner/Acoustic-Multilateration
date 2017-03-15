

import numpy

from MultiSystem import MultiSystem


def perform_test():

    source = (1, 2, 6)
    places = []
    places.append((0, 0, 0))
    places.append((-2.1, 3.1, 10.0))
    places.append(( -1, -3.1, 4.5))
    places.append((3, -5, -6))
    places.append((5, 3, 2.0001))
    numpy.transpose(places)

    multiSystem1 = MultiSystem(places)
    time = []
    i = 0
    for thing in places:
        time.append((((thing[0] - source[0]) ** 2 + (thing[1] - source[1]) ** 2 + (thing[2] - source[2]) ** 2) ** 0.5) / 340.29)
        i += 1

    x = multiSystem1._perform_multilateration()

    test = (round(x[0][0], 3), round(x[0][1], 3), round(x[0][2], 3))

    assert (numpy.array_equal(test, source))



# Main

perform_test()

# End main
