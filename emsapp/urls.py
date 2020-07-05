from django.urls import path

from emsapp import views

urlpatterns=[
    path('post/',views.RegisterAPIView.as_view()),
    path('emp/',views.EmpView.as_view()),
    path('emp/<str:id>',views.EmpView.as_view()),
]