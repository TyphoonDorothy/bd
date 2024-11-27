from my_project.movies.routes.actor_routes import actor_bp
from my_project.movies.routes.director_routes import director_bp
from my_project.movies.routes.studio_routes import studio_bp
from my_project.movies.routes.movie_routes import movie_bp
from my_project.movies.routes.fact_routes import fact_bp
from ..routes.genre_routes import genre_bp
from ..routes.festival_routes import festival_bp
from ..routes.award_routes import award_bp
from ..routes.review_routes import review_bp
from ..routes.rating_routes import rating_bp
from ..routes.actors_in_movie_routes import actors_in_movie_bp
from ..routes.movie_genre_routes import movie_genre_bp
from ..routes.movie_festival_routes import movie_festival_bp
from ..routes.movie_award_routes import movie_award_bp
from ..routes.nomination_routes import nomination_bp


def register_routes(app):
    app.register_blueprint(actor_bp, url_prefix='/api')
    app.register_blueprint(director_bp, url_prefix='/api')
    app.register_blueprint(studio_bp, url_prefix='/api')
    app.register_blueprint(movie_bp, url_prefix='/api')
    app.register_blueprint(fact_bp, url_prefix='/api')
    app.register_blueprint(genre_bp, url_prefix='/api')
    app.register_blueprint(festival_bp, url_prefix='/api')
    app.register_blueprint(award_bp, url_prefix='/api')
    app.register_blueprint(review_bp, url_prefix='/api')
    app.register_blueprint(rating_bp, url_prefix='/api')
    app.register_blueprint(actors_in_movie_bp, url_prefix='/api')
    app.register_blueprint(movie_genre_bp, url_prefix='/api')
    app.register_blueprint(movie_festival_bp, url_prefix='/api')
    app.register_blueprint(movie_award_bp, url_prefix='/api')
    app.register_blueprint(nomination_bp, url_prefix='/api')
