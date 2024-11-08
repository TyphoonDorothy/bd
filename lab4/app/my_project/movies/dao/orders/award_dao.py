from ..general_dao import GeneralDAO


class AwardDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Award

    def __init__(self):
        super().__init__(self.Award)
