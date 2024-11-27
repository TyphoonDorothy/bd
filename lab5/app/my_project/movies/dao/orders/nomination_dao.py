from ..general_dao import GeneralDAO


class NominationDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Nomination

    def __init__(self):
        super().__init__(self.Nomination)
