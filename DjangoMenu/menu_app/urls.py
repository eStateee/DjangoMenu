from django.urls import path
from menu_app.views import main, menu

urlpatterns = [
    path('', main, name='main'),
    path('<path:path>/', menu, name='menu'),
]
