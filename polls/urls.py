from django.urls import path

from . import views

urlpatterns = [
# (...manter tudo o que já existe…)
#path('perguntas/list', views.ultimas_perguntas, name='polls_list'), 
#path('pergunta/add', views.QuestionCreateView.as_view(), name="poll_add"),
#$path('pergunta/<int:pk>/edit',views.QuestionUpdateView.as_view(),name="poll_edit"),
]


urlpatterns = [
    # class based views
    path('listar', views.QuestionListView.as_view(), name="question-list"),
    path('cadastrar', views.QuestionCreateView.as_view(), name="question-create"),
    path('<int:pk>', views.QuestionDetailView.as_view(), name="question-detail"),
    path('<int:pk>/deletar', views.QuestionDeleteView.as_view(), name='question-delete')
]