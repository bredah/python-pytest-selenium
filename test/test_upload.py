"""TBD
Since 2022
"""

from test_base import TestBase
from src.core.environment import Environment as env
from src.core.helper import Helper
from src.page.upload_page import UploadPage
import calendar
import time


class TestUpload(TestBase):
    """
    Test Example
    """

    def setup_class(self):
        super().setup_class(self)
        self.upload_page = UploadPage(self.driver)

    def test_upload_file(self):
        temp_file = self.__generate_file()

        self.upload_page.open()
        self.upload_page.upload(temp_file[0])

        result = self.upload_page.get_info()

        assert result[0] == "File Uploaded!"
        assert result[1] == temp_file[1]

    def __generate_file(self) -> tuple:
        file_name = "{0}.txt".format(calendar.timegm(time.gmtime()))
        file_path = "{0}/{1}".format(
            Helper.temp_folder(), file_name)
        file = open(file_path, "w+")
        file.close()
        return (file_path, file_name)
