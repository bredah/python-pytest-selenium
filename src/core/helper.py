import tempfile


class Helper(object):

    @staticmethod
    def temp_folder() -> str:
        return tempfile.gettempdir()
