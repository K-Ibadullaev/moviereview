from django.urls import path
from . import views
urlpatterns = [
path('<int:movie_id>', views.detail,
name='detail'),
path('<int:movie_id>/create', views.createreview,
name='createreview'),
path('<int:movie_id>/update', views.updatereview,
name='updatereview'),
path('review/<int:review_id>/delete',
views.deletereview,
name='deletereview'),

]