from math import sin, cos, pi


class Polygon:
    def __init__(self, n_edges, r):

        self.edges = n_edges
        self.radius = r
        self.vertices = n_edges
        self.init_parameters()

    def init_parameters(self):
        _ = self.edge_length
        _ = self.interior_angle
        _ = self.apothem
        _ = self.area
        _ = self.perimeter

    @property
    def edges(self):
        return self._edges

    @property
    def radius(self):
        return self._radius

    @edges.setter
    def edges(self, n_edges):
        if not isinstance(n_edges, (int, float)):
            raise ValueError
        if n_edges < 3:
            raise ValueError

        self._edges = n_edges
        self._vertices = n_edges
        self._edge_length = None
        self._interior_angle = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vert):
        if not isinstance(vert, (int, float)):
            raise ValueError
        if vert < 3:
            raise ValueError

        self._edges = vert
        self._vertices = vert
        self._edge_length = None
        self._interior_angle = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @radius.setter
    def radius(self, r):
        if not isinstance(r, (int, float)):
            raise ValueError
        if r < 0:
            raise ValueError
        self._radius = r
        self._edge_length = None
        self._interior_angle = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def edge_length(self):
        if self._edge_length is None:
            self._edge_length = 2 * self._radius * sin(pi / self._edges)

        return self._edge_length

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle = (self._edges - 2) * 180 / self._edges
        return self._interior_angle

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._radius * cos(pi / self._edges)
        return self._apothem

    @property
    def area(self):
        if self._apothem is None:
            _ = self.apothem
        if self._edge_length is None:
            _ = self.edge_length
        if self._area is None:
            self._area = 0.5 * self._edges * self._edge_length * self._apothem
        return self._area

    @property
    def perimeter(self):
        if self._edge_length is None:
            _ = self.edge_length
        if self._perimeter is None:
            self._perimeter = self._edges * self._edge_length
        return self._perimeter

    def __repr__(self):
        return f"A regular polygon with {vars(self)}"

    def __eq__(self, other):
        return (self.vertices == other.vertices) and (self.radius == other.radius)

    def __gt__(self, other):
        return self.vertices > other.vertices
