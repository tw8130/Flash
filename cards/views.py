from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .forms import FlashCreationForm,NewsLetterForm,DeckCreateForm
from .models import FlashCards,Category,Deck
from .email import send_welcome_email
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
# Create your views here.
def welcome(request,deck_id):
    deck = Deck.objects.get(id=deck_id)
    # context = {'deck': deck,
    #            'flashcards': deck.flashcards.all()}
    flash_cards=FlashCards.objects.all()
    form = NewsLetterForm()
    return render(request, 'flashcard_view.html' ,{"flash_cards":flash_cards, "letterForm":form})

def deck_create_view(request):
    """
    Adds a deck to the database if request.method is POST, otherwise returns a render for the form.
    """

    if request.method == 'POST':
        form = DeckCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_deck = Deck(deck_name=name,date_created=datetime.now())
            new_deck.save()
            return HttpResponseRedirect('/decks/')
    return render(request, 'deck_create.html', {'form': form})

def flash_creation(request):
    current_user=request.user
    if request.method == 'POST':
        form=FlashCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('post_card')
    else:
        form=FlashCreationForm()
    return render(request, 'create_card.html', {'form': form})


def flash_detail(request, flash_id):
    flash_card = FlashCards.objects.get(id=flash_id)
    return render(request, 'card_detail.html', {'flash_card':flash_card})

def delete_flash_card(request, flash_id):
    flash_card = FlashCards.objects.get(id=flash_id)
    if request.method == 'POST':
        flash_card.delete()
        return redirect('welcome')
    return render(request, 'delete_card.html', {'flash_card':flash_card})

def update_flash_card(request, flash_id):
    flash_card = FlashCards.objects.get(id=flash_id)
    form = FlashCreationForm(request.POST or None, instance=flash_card)
    if form.is_valid():
        form_save = form.save(commit=False)
        form_save.date_updated = timezone.now()
        form_save.save()
        return redirect('welcome')
    return render(request, 'update_card.html', {'form':form})

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

# def search_card(request):
#     if 'flashcard' in request.GET and request.GET ["flashcard"]:
#         search_term = request.GET.get("flashcard")
#         searched_flashcards = FlashCard.search_project_by_title(search_term)
#         message = f'{search_term}'

#         return render(request, 'search.html', {"message":message, "flashcards":searched_flashcards})

#     else:
#         message = "No search results yet!"
#         return render (request, 'search.html', {"message": message})