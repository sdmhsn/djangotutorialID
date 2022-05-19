from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),  # http://127.0.0.1:8000/polls/
    path('', views.IndexView.as_view(), name='index'),  # cbv

    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # cbv. DetailView mensyaratkan parameter yang diinput harus menggunakan keyword <int:pk> untuk primary key berupa integer, bukan <int:question_id>

    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # cbv. DetailView mensyaratkan parameter yang diinput harus menggunakan keyword <int:pk> untuk primary key berupa integer, bukan <int:question_id>

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
