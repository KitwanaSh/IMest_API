from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def json_response(request):
    return JsonResponse({"name": "Driver"})

def http_response(request):
    return HttpResponse("<h1>Hello Driver you are welcome</h1>")

# name: your name, emai: your email, phone_number: your phone number
# Register the view function on a path called profile

def userProfile(request):
    jsR = {
        "name": "Ezechiel",
        "email": "ezechiel@email.com",
        "phone_number": "+243852659448"
    }
    return JsonResponse(jsR)

def filter_queries(request):
    dataset = [
    {
        "id": 1,
        "title": "Escalate The Room",
        "description": "Hereunder you will find all the information you need - along with some inspirations - to create engaging posts or send attractive messages. Remember that the blurbs below are merely suggestions - your creativity, passion and belief in the ALX SE sauce is the real fuel you need!",
        "status": "High",
        "submitted_by": "Ezechiel",
    },
    {
        "id": 2,
        "title": "Search for peace",
        "description": "Hereunder you will find all the information you need ",
        "status": "Low",
        "submitted_by": "Danial",
    },
    {
        "id": 3,
        "title": "Denied By",
        "description": "Postponement is a killer of great ideas!",
        "status": "Medium",
        "submitted_by": "Batistusta",
    },
    
]
    
    return JsonResponse(dataset)