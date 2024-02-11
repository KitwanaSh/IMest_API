from django.db import models
from users.models import Cohort, IMuser

class Course(models.Model):
    """ Class representation of courses """
    name = models.CharField(max_length=50)
    descriptionn = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return  self.name
    
class ClassSchedule(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    start_date_and_time = models.IntegerField()
    end_date_and_time = models.IntegerField()
    is_repeated = models.BooleanField()
    repeat_frequency = models.IntegerField(default=2)
    is_active = models.BooleanField()
    organizer = models.CharField(max_length=60, blank=True, null=True)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name="class_cohort")
    venue = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.title
    
class ClassAttendance(models.Model):
    class_schedule = models.ManyToManyField(ClassSchedule, related_name="attendance_schel")
    attendee = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name="attendee_user")
    is_present = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name="author_attendee")
    
    
    def __str__(self):
        return f"{self.class_schedule} to {self.attendee}"

    
class Query(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    submitted_by = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name="submitQuery_user")
    assigned_to = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name="assignQuery_user")
    resolution_status = models.CharField(max_length=20, choices=[
        ("PENDING", "PENDING"), ("IN_PROGRESS", "IN_PROGRESS"), ("DECLINED", "DECLINED"), ("RESOLVED", "RESOLVED")
        ])
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name="author_query")

    def __str__(self):
        return self.title

    
class QueryComment(models.Model):
    query = models.ForeignKey(Query, related_name="comment_query", on_delete=models.CASCADE)
    comment = models.CharField(max_length=1500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name="author_queryComment")

    def __str__(self):
        return self.query
    