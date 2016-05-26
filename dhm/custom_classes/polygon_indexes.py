# coding=utf-8


class PolygonIndexes:
    """

    Класс, который используется в качестве ключа для словаря с полигонами.
    Унимальными должна быть пара значений - индекс полигона по горизонтали и индекс полигона по вертикали.

    """
    def __init__(self, x_index, y_index):
        self.x_index = x_index
        self.y_index = y_index

    def __hash__(self):
        return hash((self.x_index, self.y_index))

    def __eq__(self, other):
        return (self.x_index, self.y_index) == (other.x_index, other.y_index)
