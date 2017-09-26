from src.controllers import User, Help


class RoutesRegistration:
    def register_in_app(self, app):
        app.register_blueprint(User.user_controller)
        app.register_blueprint(Help.help_controller)

        return app
