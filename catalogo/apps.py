from django.apps import AppConfig


class CatalogoConfig(AppConfig):
    name = 'catalogo'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        # Vercel: filesystem is read-only. Disconnect the signal that updates
        # last_login on the User model every time someone logs in — that write
        # would crash with "attempt to write a readonly database".
        try:
            from django.contrib.auth.signals import user_logged_in
            from django.contrib.auth.models import update_last_login
            user_logged_in.disconnect(update_last_login)
        except Exception:
            pass
