from ..general_controller import GeneralController
from my_project.movies.controller.__init__ import FestivalService


class FestivalController(GeneralController):
    def __init__(self):
        super().__init__(FestivalService())
