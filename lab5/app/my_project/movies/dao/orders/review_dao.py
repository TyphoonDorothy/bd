from ..general_dao import GeneralDAO


class ReviewDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Review

    def __init__(self):
        super().__init__(self.Review)
