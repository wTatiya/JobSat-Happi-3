from django.shortcuts import render


def index(request):
    """Render the landing page for the Happinometer app."""

    return render(request, "main/index.html")
