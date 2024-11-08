from ..general_service import GeneralService
from my_project.movies.service.__init__ import Rating, RatingDAO


class RatingService(GeneralService):
    def __init__(self):
        super().__init__(RatingDAO(), Rating)
