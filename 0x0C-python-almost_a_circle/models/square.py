#!/usr/bin/python3
"""Created a class square
   The setter should assign (in this order)
   the width and the height - with the same value
   The setter should have the same value validation
   as the Rectangle for width and height
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Prints [Square] (<id>) <x>/<y> - <size>
        """
        return"[{:s}] ({:d}) {:d}/{:d} - {:d}".\
            format(self.__class__.__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter size
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """if args set attributes id, width, height, x , y
           if no args set attributes with kwargs
        """

        kwargs.update(width=kwargs.get("size", self.width),
         height=kwargs.get("size", self.height))
        if len(args) > 2:
            args = [*args[:1], args[1], *args[1:]]
        super().update(*args, **kwargs)

    def to_dictionary(self):
        """Return dictionary representation"""

        dic = {}
        dic["id"] = self.id
        dic["x"] = self.x
        dic["size"] = self.size
        dic["y"] = self.y
        return dic
