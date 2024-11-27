from flask import request, jsonify
from ..general_controller import GeneralController
from my_project.movies.controller.__init__ import GenreService


class GenreController(GeneralController):
    def __init__(self):
        super().__init__(GenreService())

    def create(self):
        data = request.get_json()
        name = data.get("name")
        if not name:
            return jsonify({"error": "Name is required"}), 400
        genre_id = self.service.create_genre(name)
        return jsonify({"id": genre_id, "name": name}), 201

    def insert_genres(self):
        self.service.insert_genres()
        return jsonify({"message": "Genres inserted successfully."}), 20