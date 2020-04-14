from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Member:
    def __init__ (self,name,position,email,phone,description):
        self.name = name
        self.position = position
        self.email = email
        self.phone = phone
        self.description = description

members = [
    Member('Yvonne', 'Founder', 'yvonnewjy@hotmail.com', '416-000-0000', 'Love singing and watch drama'),
    Member('XYZ', 'Member', 'member@hotmail.com', '100-000-0000', 'Love food' )
]

def home(request):
    return HttpResponse('<h1>Hellow</h1>')

def about(request):
    return render(request, 'about.html')

def members_index(request):
    return render(request, 'members/index.html', {'members': members})