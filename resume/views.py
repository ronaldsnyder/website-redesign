# Create your views here.

from django.shortcuts import render, get_object_or_404
from resume.models import Employer, Job, Responsibility, Accomplishment

def index(request):
#    posts = Post.objects.filter(published=True)
    return render(request, 'resume/index.html')

def experience(request):
    employer = Employer.objects
    job = Job.objects
    resp = Responsibility.objects
    accomp = Accomplishment.objects
    return render(request, 'resume/experience.html', {'employer':employer, 'job':job, 'responsibility': resp,
                                                      'accomplishment': accomp})
