from django.urls import path

from .views import CalculateTimeView, TrackView

app_name = 'track_app'

urlpatterns = [
  	path('tracks/', TrackView.as_view(), name='track-upload'),
  	path('tracks/<id>/calculate-start-time/', CalculateTimeView.as_view(), name='calculate-start-time'),
]
