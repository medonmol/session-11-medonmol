
<h2 align='center'> Assignment - Iterable:-  Polygon Sequence </h3>

## Objective:
Take the custom polygon class from session 10, and convert it into an iterable

## Solution

The `PolygonSequence` class can be converted to an `iterable` by adding an `iter` method, which calls the `PolygonIter` class. The `PolygonIter` class is an `iterator` (the `__iter__` method returns `self`), which implements the `__next__` and `__iter__` methods.

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


A Deepnote notebook demonostrating the changes to the PolygonSequence class can be found [here](https://deepnote.com/project/EPAi3-session11-1UYAa-jIRQmQzYhA-3OeDQ/%2Fnotebook.ipynb)
