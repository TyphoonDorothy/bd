from ..general_dao import GeneralDAO


class RatingDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Rating

    def __init__(self):
        super().__init__(self.Rating)
