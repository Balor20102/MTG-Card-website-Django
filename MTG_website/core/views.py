from django.shortcuts import render
from django.views.generic import View
from mtgsdk import Card

# Create your views here.
class HomePageView(View):
    def get(self, request, *args, **kwargs):
        content = {
            "card": Card.where(set='ktk').where(subtypes='warrior,human').all()
        }
        return render(request, "core/home.html", content)