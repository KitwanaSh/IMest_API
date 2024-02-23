from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from datetime import datetime


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

@api_view(['GET'])
def fetch_class_schedules(request):
    queryset = ClassSchedule.objects.all()
    serializer = ClassScheduleSerializer(queryset, many=True)

    return Response({"data": serializer.data}, status.HTTP_200_OK)

@api_view(['POST'])
def create_class_schedule(request):
    title = request.data.get("title")
    description = request.data.get("description")
    start_date_and_time = request.data.get("start_date_and_time")
    end_date_and_time = request.data.get("end_date_and_time")
    cohort_id = request.data.get("cohort_id")
    venue = request.data.get("vanue")
    facilitator_id = request.data.get("facilitator_id")
    is_repeated = request.data.get("is_repeated")
    repeate_frequency = request.data.get("repeate_frequency")
    course_id = request.data.get("course_id")
    meeting_type = request.data.get("meeting_type")


    if not title:
        return Response({"message": "My friend, send me a title"}, status.HTTP_400_BAD_REQUEST)
    
    cohort = None
    facilitator = None
    course = None

    try:
        cohort = Cohort.objects.get(id=cohort_id)
    except Cohort.DoesNotExist:
        return Response({"message": "Body, this cohort does not exist!"}, status.HTTP_400_BAD_REQUEST)
    
    try:
        facilitator = IMUser.objects.get(id=facilitator_id)
    except IMUser.DoesNotExist:
        return Response({"message": "Body, this facilitator does not exist!"}, status.HTTP_400_BAD_REQUEST)
    
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"message": "Body, this course does not exist!"}, status.HTTP_400_BAD_REQUEST)
    

    class_schedule = ClassSchedule.objects.create(
        title=title,
        description=description,
        venue=venue,
        is_repeated=is_repeated,
        repeate_frequency=repeate_frequency,
        start_date_and_time=datetime.now(),
        end_date_and_time=datetime.now(),
        facilitator=facilitator,
        cohort=cohort,
        course=course,
        organizer=facilitator
    )

    class_schedule.save()
    serializer = ClassScheduleSerializer(class_schedule, many=False)

    return Response({"message": "Schedule successfully created", "data": serializer.data}, status.HTTP_200_OK)