from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('delete/<question_id>',views.clean_questions, name ='clean_questions'),
    path('add/<question_text>',views.add_question, name ='add_question'),
    path('add/<question_id>/<choiceText>',views.add_choice, name ='add_choice'),
    path('all',views.show_questions, name ='show_questions')
    ]
