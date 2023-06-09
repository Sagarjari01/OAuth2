from django.urls import path
from .views import GoogleCalendarInitView, GoogleCalendarRedirectView

urlpatterns = [
    path('rest/v1/calendar/init/', GoogleCalendarInitView, name='google_permission'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView, name='google_redirect')
]
