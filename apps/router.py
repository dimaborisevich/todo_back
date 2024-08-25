from django.urls import path, include


urlpatterns = [
    path('taskas/', include('apps.todo.urls')),
]