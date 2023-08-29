from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),


    path ('cadastrar', views.QuestionCreateView.as_view(), name ="question-create")
]






urlpatterns = [
# (...manter tudo o que já existe…)
#path('perguntas/list', views.ultimas_perguntas, name='polls_list'), 
#path('pergunta/add', views.QuestionCreateView.as_view(), name="poll_add"),
#$path('pergunta/<int:pk>/edit',views.QuestionUpdateView.as_view(),name="poll_edit"),
]