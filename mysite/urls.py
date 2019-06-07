from django.contrib import admin
from django.urls import path

from pools import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('question/<int:question_id>', views.question, name='question'),
]
