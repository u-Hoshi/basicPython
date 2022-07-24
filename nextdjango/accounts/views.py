from django.shortcuts import render

# Create your views here.
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class GoogleLoginView(SocialLoginView):
  adapter_class = GoogleOAuth2Adapter
  client_class = OAuth2Client
  