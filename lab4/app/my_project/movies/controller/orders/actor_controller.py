from my_project.movies.controller.general_controller import GeneralController
from my_project.movies.controller.__init__ import ActorService


class ActorController(GeneralController):
    def __init__(self):
        super().__init__(ActorService())
