from src.class_hh_api import HeadHunterAPI
from src.class_sj_api import SuperJobAPI


class MainLoop:
    """Этот класс предназначен для взаимодействия
     с пользователем в консоли."""

    def __init__(self):
        self.hh_api = HeadHunterAPI()
        self.sj_api = SuperJobAPI()

