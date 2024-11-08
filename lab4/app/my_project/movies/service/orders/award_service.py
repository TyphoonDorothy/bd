from ..general_service import GeneralService
from my_project.movies.service.__init__ import Award, AwardDAO


class AwardService(GeneralService):
    def __init__(self):
        super().__init__(AwardDAO(), Award)
