from ..general_service import GeneralService
from my_project.movies.service.__init__ import Fact, FactDAO


class FactService(GeneralService):
    def __init__(self):
        super().__init__(FactDAO(), Fact)
