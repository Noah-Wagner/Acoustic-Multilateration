

import numpy

from MultiSystem import MultiSystem


def perform_test():

    source = (1, 2, 4)
    places = []
    places.append((0, 0, 0))
    places.append((-2.1, 3.1, 10.0))
    places.append(( -1, -3.1, 4.5))
    places.append((3, -5, -6))
    places.append((5, 3, 2.0001))
    numpy.transpose(places)

    multiSystem1 = MultiSystem(places)
    i = 0
    for thing in places:
        multiSystem1.addTime((((thing[0] - source[0]) ** 2 + (thing[1] - source[1]) ** 2 + (thing[2] - source[2]) ** 2) ** 0.5) / 340.29, i)
        i += 1

    x = multiSystem1.perform_multilateration()
    print(x)


# Main

perform_test()

# End main
