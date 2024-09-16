from django.shortcuts import render
import requests
from .models import Book   
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from icecream import ic


class MainView(ListView):
    model = Book
    template_name = 'bookmarket/main.html'
    context_object_name = "books"

    def get_queryset(self):
        query = self.request.GET.get("q")

        if query:
            return Book.objects.filter(
                Q(name__icontains=query) | Q(author__icontains=query)
            )
        
        return Book.objects.all()

