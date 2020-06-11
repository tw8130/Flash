from django.contrib import admin
from .models import Deck,FlashCards,Category

# Register your models here.
admin.site.register(Deck)
admin.site.register(FlashCards)
admin.site.register(Category)
