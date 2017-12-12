from rest_framework import views, status, permissions
from rest_framework.response import Response

from django.conf import settings

import requests


KEY = settings.SOCIAL_AUTH_FACEBOOK_KEY
SECRET = settings.SOCIAL_AUTH_FACEBOOK_SECRET
REDIRECT_URI = 'https://katrina.tw/' #settings.FACEBOOK_REDIRECT_URI

class AccessView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if 'code' in request.query_params:
            code = request.query_params['code']
            url = 'https://graph.facebook.com/v2.11/oauth/access_token?client_id={app_id}&redirect_uri={redirect_uri}&client_secret={app_secret}&code={code}'.format(app_id=KEY, redirect_uri=REDIRECT_URI, app_secret=SECRET, code=code)
            resp = requests.get(url)
            resp.encoding = 'utf-8'
            body = resp.json()
            if 'access_token' in body:
                return Response(status=status.HTTP_200_OK, data=body)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=body)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'Missing parameter "code".'})
