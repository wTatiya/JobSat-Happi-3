from django.shortcuts import render


def home(request):
    """Render the main landing page template."""
    return render(request, 'main/index.html')
