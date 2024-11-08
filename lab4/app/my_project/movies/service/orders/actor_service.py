from my_project.movies.service.general_service import GeneralService
from my_project.movies.service.__init__ import Actor
from my_project.movies.service.__init__ import ActorDAO

class ActorService(GeneralService):
    def __init__(self):
        super().__init__(ActorDAO(), Actor)