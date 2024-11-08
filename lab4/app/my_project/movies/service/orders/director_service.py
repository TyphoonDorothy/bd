from my_project.movies.service.general_service import GeneralService
from my_project.movies.service.__init__ import Director, DirectorDAO


class DirectorService(GeneralService):
    def __init__(self):
        super().__init__(DirectorDAO(), Director)


    def get_movies_by_director_id(self, director_id):
        return DirectorDAO.get_movies_by_director_id(director_id)
