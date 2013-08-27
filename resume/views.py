# Create your views here.

from django.shortcuts import render, get_object_or_404
from resume.models import Employer, Job, Responsibility, Accomplishment, HardSkill, SoftSkill, Education

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

def skills(request):
    hardskill = HardSkill.objects
    softskill = SoftSkill.objects
    return render(request, 'resume/skills.html', {'hardskill':hardskill, 'softskill':softskill, })

def education(request):
    bs = Education.objects.get(id=1)
    ass = Education.objects.get(id=2)
    return render(request, 'resume/education.html', {'bs':bs,'ass':ass,})
