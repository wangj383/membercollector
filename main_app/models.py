from django.db import models
from datetime import date
from django.urls import reverse

STATUS = (
    ('A', "assigned"),
    ('P', "in progress"),
    ('C', "completed")
)

class Member(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(default=None)
    position = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    @property
    def age(self):
        return int((date.today() - self.birthday).days/365.2425)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('member_detail', kwargs={"member_id": self.id})

class Task(models.Model):
    date = models.DateField()
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=STATUS[0][0]
    )
    task = models.CharField(max_length=300)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.task} is {self.get_status_display()} on {self.date}"




