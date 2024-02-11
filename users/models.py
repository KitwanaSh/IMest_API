from django.db import models


class IMuser(models.Model):
    """ IMuser table """
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    is_active = models.BooleanField()
    user_type = models.CharField( max_length=20, choices=[
        ("EIT", "EIT"), ("TEACHING_FELLOW", "TEACHING_FELLOW"), ("ADMIN_STAFF", "ADMIN_STAFF"), ("ADMIN", "ADMIN")
        ]
    )

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    

class Cohort(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(default=2024)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name="author_name")

    def __str__(self):
        return self.name

class CohortMember(models.Model):
    name = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name="cohort_name")
    member = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name="cohort_members")
    is_active = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name="member_userType")

    def __str__(self):
        return self.name
