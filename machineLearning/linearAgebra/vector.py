#!/usr/bin/python3
class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def multiScalar(self,v):
        new_coordinates = [x*v for x in self.coordinates ]
        return new_coordinates


    def minus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return new_coordinates



    def plus(self,v):
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return new_coordinates