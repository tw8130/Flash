from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(max_length=60)

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.cat_name = update
        self.save()
    
    def get_category_id(cls, id):
        category = Category.object.get(pk = id)
        return category


    def __str__(self):
        return self.cat_name

class Deck(models.Model):
    deck_name=models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)

    def save_deck(self):
        self.save()
    
    def delete_deck(self):
        self.delete()
    
    def get_deck_id(cls, id):
        deck = Deck.object.get(pk = id)
        return deck
    
    
    def __str__(self):
        return self.deck_name

class FlashCards(models.Model):
    title = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    decks = models.ManyToManyField(Deck, related_name="flashcards")
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all_flash_cards(cls):
        flash_cards=FlashCards.objects.all()
        return flash_cards
    
    @classmethod
    def get_single_flash_card(cls, flash_id):
        flash_card=FlashCards.objects.get(id=flash_id)
        return flash_card

    @classmethod
    def search_by_category(cls,search_term):
        card = cls.objects.filter(category__cat_name__icontains=search_term)
        return card  
    
    def delete_flash_card(self):
        self.delete()
    
    def save_flash_card(self):
        self.save()

    def __str__(self):
        return self.title

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()