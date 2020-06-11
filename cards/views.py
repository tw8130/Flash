from django.shortcuts import render
from django.http  import HttpResponse,Http404
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def search_card(request):
    if 'flashcard' in request.GET and request.GET ["flashcard"]:
        search_term = request.GET.get("flashcard")
        searched_flashcards = Project.search_project_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {"message":message, "flashcards":searched_flashcards})

    else:
        message = "No search results yet!"
        return render (request, 'search.html', {"message": message})