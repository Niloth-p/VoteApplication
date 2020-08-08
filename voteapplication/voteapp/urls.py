from django.urls import path

from voteapp.views import index, detail, results

urlpatterns = [
    path('', index, name='index'),
    path('<int:candidate_id>/', detail, name='detail'),
    path('results/', results),
]