from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


monthly_challenges = {
    "january": "Eat no meat for an entire month",
    "february": "Call 1 friend everyday",
    "march": "Learn Django for 3 hours",
    "april": "Pray everyday",
    "may": "Stay off social media",
    "june": "Yoga everyday",
    "july": "medidate Everyday",
    "august": "Finish a book every week",
    "september": "Visit a relative every weekend",
    "october": "Travel with my wife",
    "november": "Save 80% of my income",
    "december": "quit alcohol"
    
    
}
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month number!")
    
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1> {challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>") 
        

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        month_path = reverse("month-challenge",args=[month])
        list_items += f"<li><a href =\" {month_path}\">{month}</a> </li>"
    
    response_data = f"<ul>{list_items}</ul>"
    
    return HttpResponse(response_data)