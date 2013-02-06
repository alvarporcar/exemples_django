# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from models import Book
from forms import ContactForm, PublisherForm

def search(request):
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(title__icontains=query) | 
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query) 
        )
        results = Book.objects.filter(qset).distinct()

    else:
        results = []

    return render_to_response("search.html",{"results":results, "query":query})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data["topic"]
            messages = form.cleaned_data["messages"]
            sender = form.cleaned_data.get("sender","noreply@example.com")
            # send_mail("Resposta del teu lloc, topic: %s" % topic,
            #        messages, sender,
            #        ["alvar.porcar@gmail.com"]
            #)
            return HttpResponseRedirect("/contact/thanks/")
    
    else:
        form = ContactForm()

    return render_to_response("contact.html",{"form":form})


def add_publisher(request):
    if request.method == "POST":
        formulario = PublisherForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/add_publisher/thanks/")
    else :
        formulario = PublisherForm()
    
    return render_to_response("add_publisher.html",{"form":formulario})

def contact_thanks(request):
    return render_to_response("contact_thanks.html")

def add_publisher_thanks(request):
    return render_to_response("add_publisher_thanks.html")

