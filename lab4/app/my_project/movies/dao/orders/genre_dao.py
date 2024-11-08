from ..general_dao import GeneralDAO


class GenreDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Genre

    def __init__(self):
        super().__init__(self.Genre)
