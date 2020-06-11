from django.urls import path
from . import views
from django.views.generic import ListView, TemplateView
from .models import Deck
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # path('', TemplateView.as_view(template_name="flashcard_view.html")),
    # path('search/',views.search_card, name='search_results'),
    path('', views.welcome, name='welcome'),
    path('post_card', views.flash_creation, name='post_card'),
    path('decks/',
                    ListView.as_view(queryset=Deck.objects.all().order_by('-date_created'),
                                     template_name='deck_list.html')),
    path('decks/<int:deck_id>/', views.welcome,name='welcome'),
    path('create/deck/', views.deck_create_view,name='create_deck'),
    path('view_card/<int:flash_id>', views.flash_detail, name='view_card'),
    path('update_card/<int:flash_id>', views.update_flash_card, name='update_card'),
    path('delete_card/<int:flash_id>', views.delete_flash_card, name='delete_card'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)