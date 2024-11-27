from ..general_controller import GeneralController
from my_project.movies.controller.__init__ import ReviewService
from flask import jsonify, request

class ReviewController(GeneralController):
    def __init__(self):
        super().__init__(ReviewService())

    def calculate_score(self):
        """Handle the calc_score function."""
        calculation_type = request.args.get("type", "").lower()
        if calculation_type not in ["max", "min", "avg", "sum"]:
            return jsonify({"error": "Invalid calculation type"}), 400
        try:
            score = self.service.calculate_score(calculation_type)
            return jsonify({"calculation_type": calculation_type, "score": score}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 500
