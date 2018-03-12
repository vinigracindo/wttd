from django.contrib import admin
from django.urls import path, include

from eventex.core.views import speaker_detail, talk_list, home

urlpatterns = [
    path('', home, name='home'),
    path('inscricao/', include(('eventex.subscriptions.urls', 'eventex.subscriptions'))),
    path('palestras/', talk_list, name='talk_list'),
    path('palestrantes/<int:pk>/', speaker_detail, name='speaker_detail'),
    path('admin/', admin.site.urls),
]
