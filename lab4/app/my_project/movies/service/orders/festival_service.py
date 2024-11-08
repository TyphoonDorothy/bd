from ..general_service import GeneralService
from my_project.movies.service.__init__ import Festival, FestivalDAO


class FestivalService(GeneralService):
    def __init__(self):
        super().__init__(FestivalDAO(), Festival)
