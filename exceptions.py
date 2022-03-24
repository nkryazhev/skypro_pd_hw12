class PictureWrongFileType(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class DataLayerError(Exception):
    def __init__(self, message=None):
        super().__init__(message)
