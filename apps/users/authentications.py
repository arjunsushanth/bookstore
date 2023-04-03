from .models import User
from rest_framework import authentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.exceptions import ValidationError
from rest_framework import exceptions


class CustomAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        try:
            if 'Authorization' not in request.headers:
                raise ValidationError({"error": "please login"})

            elif request.META.get('HTTP_AUTHORIZATION') == "":
                raise ValidationError({"error": "please add authorization token"})

            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
            user = User.objects.get(id=valid_data['user_id'])
            request.user = user
            return (user, None)
        except:
            raise exceptions.AuthenticationFailed('Please add valid token')