from ..general_service import GeneralService
from my_project.movies.service.__init__ import Studio, StudioDAO


class StudioService(GeneralService):
    def __init__(self):
        super().__init__(StudioDAO(), Studio)

    def get_movies_by_studio_id(self, studio_id):
        return StudioDAO.get_movies_by_studio_id(studio_id)
