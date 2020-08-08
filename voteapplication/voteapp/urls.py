from django.urls import path

from voteapp.views import index, detail, results
from voteapp.admin_actions import add_cand, delete_cand
from voteapp.candidate_actions import edit_cand

urlpatterns = [
    path('', index, name='index'),
    path('<int:candidate_id>/', detail, name='detail'),
    path('results/', results),
    path('add_candidate/', add_cand),
    path('delete_candidate/', delete_cand),
    path('edit_details', edit_cand),
]