from functools import lru_cache
from Polygon_session_11 import Polygon


class PolygonSequence:
    def __init__(self, max_edge, radius):
        self.max_edge = max_edge
        self.radius = radius
        self.ratio = {}

    def init_parameters(self):
        _ = self.max_edge
        _ = self.radius

    @property
    def max_edge(self):
        return self._max_edge

    @max_edge.setter
    def max_edge(self, new_max_edge):
        if not isinstance(new_max_edge, (int, float)):
            raise ValueError
        if new_max_edge < 3:
            raise ValueError

        self._max_edge = new_max_edge

    @property
    def radius(self):

        return self._radius

    @radius.setter
    def radius(self, rad):
        if not isinstance(rad, (int, float)):
            raise ValueError
        if rad < 0:
            raise ValueError

        self._radius = rad

    def __repr__(self):
        return f"Polygon Sequence class with max_edge = {self.max_edge} and common radius = {self.radius}"

    def __len__(self):
        return self.max_edge - 2

    def __getitem__(self, idx):
        if isinstance(idx, int):
            if idx >= 0:
                if idx < 3:
                    idx = 3
                return PolygonSequence.get_poly(idx, self.radius)

            else:
                idx = self.max_edge + idx
                if idx < 0 or idx >= self.max_edge:
                    raise IndexError
                return PolygonSequence.get_poly(idx + 1, self.radius)
        else:
            start, end, skip = idx.indices(self.max_edge + 1)
            start = start if start > 3 else 3
            end = end if end >= 3 else 2
            return [
                PolygonSequence.get_poly(i, self.radius)
                for i in range(start, end, skip)
            ]

    @staticmethod
    @lru_cache(16)
    def get_poly(n, radius):
        return Polygon(n, radius)

    @property
    @lru_cache(1)
    def max_efficiency(self):
        for i in range(3, self.max_edge + 1):
            poly = self.__getitem__(i)
            self.ratio[i] = poly.area * 1.0 / poly.perimeter
        max_key = max(self.ratio, key=self.ratio.get)
        # return f"max_efficiency_polygon_edge: {max_key}, area/perimeter ratio : {self.ratio[max_key]}"
        return self.get_poly(max_key, self.radius)

    def __iter__(self):
        return self.PolygonIter(self)

    class PolygonIter:
        def __init__(self, polygon_object):
            self._polygon_object = polygon_object
            self._idx = 3

        def __iter__(self):
            return self

        def __next__(self):
            if self._idx > self._polygon_object.max_edge:
                raise StopIteration
            else:
                poly = Polygon(self._idx, self._polygon_object._radius)
                self._idx += 1
                return poly


if __name__ == "__main__":
    seq = PolygonSequence(10, 5)
    for s in seq:
        print(s)
