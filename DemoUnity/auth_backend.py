# auth_backend.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db import connection
from django.contrib.auth.hashers import check_password

class MySQLBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT password FROM users WHERE username = %s", [username])
            row = cursor.fetchone()
            if row is not None:
                db_password = row[0]
                if check_password(password, db_password):
                    try:
                        user = User.objects.get(username=username)
                    except User.DoesNotExist:
                        user = User(username=username)
                        user.save()
                    return user
        finally:
            cursor.close()
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
