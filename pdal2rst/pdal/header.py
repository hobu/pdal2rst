from .exceptions import ConverterError
from .object import BaseObject


class Header(BaseObject):
    """
    Represents PDAL info Header Object
    """

    def __init__(self, obj, **kwargs):
        super(Header, self).__init__(obj, **kwargs)
        self.description = obj.get('description')
