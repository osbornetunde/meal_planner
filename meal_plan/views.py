from django.shortcuts import render

def index(request):
    """The homepage for meal plan"""
    return render(request, 'meal_plan/index.html')
