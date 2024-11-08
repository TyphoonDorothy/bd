from ..general_service import GeneralService
from my_project.movies.service.__init__ import Review, ReviewDAO


class ReviewService(GeneralService):
    def __init__(self):
        super().__init__(ReviewDAO(), Review)
