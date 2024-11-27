from my_project.movies.dao.general_dao import GeneralDAO


class ActorDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Actor
    def __init__(self):
        super().__init__(self.Actor)
