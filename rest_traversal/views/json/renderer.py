from pyramid.renderers import JSON as PyramidJSON


class JSON(PyramidJSON):

    def __init__(self):
        self.add_adapter()
