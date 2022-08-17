from django.urls import path
from .views import IndexView, PersonUpdateView, PersonListView


urlpatterns = [
    path('', IndexView.as_view(), name='account'),
    path('<pk>/update', PersonUpdateView.as_view(), name='person_update'),
    path('person_list/', PersonListView.as_view(), name='person_list')
]