from ..general_dao import GeneralDAO


class FestivalDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Festival

    def __init__(self):
        super().__init__(self.Festival)
