from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Member, Event, Task, Photo
from .forms import TaskForm

import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'memcollec'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def members_index(request):
    members = Member.objects.all()
    return render(request, 'members/index.html', {'members': members})

@login_required
def member_detail(request, member_id):
    member = Member.objects.get(id=member_id)
    events_member_doesnt_have = Event.objects.exclude(id__in = member.event.all().values_list('id'))
    taskform = TaskForm()
    return render(request, 'members/detail.html', {'member': member, 'taskform': taskform, 'events': events_member_doesnt_have})

class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    fields = ['name','birthday','position','email','phone','description']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    fields = ['name','birthday','position','email','phone','description']

class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    success_url = '/members/'

@login_required
def add_task(request, member_id):
    taskform = TaskForm(request.POST)
    if taskform.is_valid():
        new_task=taskform.save(commit=False)
        new_task.member_id=member_id
        new_task.save()
    return redirect('member_detail', member_id = member_id)

@login_required
def associate_event(request, member_id,event_id):
    Member.objects.get(id=member_id).event.add(event_id)
    return redirect('member_detail', member_id=member_id)

@login_required
def unassociate_event(request, member_id, event_id):
    Member.objects.get(id=member_id).event.remove(event_id)
    return redirect('member_detail', member_id=member_id)
   
@login_required
def add_photo(request, member_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, member_id=member_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('member_detail', member_id=member_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('members_index')
    else:
      error_message = 'Invalid sign up, please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)