from ..general_dao import GeneralDAO


class FactDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Fact

    def __init__(self):
        super().__init__(self.Fact)
