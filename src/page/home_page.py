from src.page.base_page import BasePage

class HomePage(BasePage):
  
  def __init__(self):
      super().__init__()

  def open(self):
      super().open("/index.php")
  