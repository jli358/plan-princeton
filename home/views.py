from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Concentration
from django.shortcuts import render_to_response
from home.models import Concentration
from home.models import User
from home.models import Course
from home.models import CourseManager

# Create your views here.
@login_required
def index(request):
	# test = Concentration.objects.get(name="Chemistry").get_reqs()
	# print(test)

	allconcentrations = []
	for conc in Concentration.objects.all():
		allconcentrations.append(conc.name)
	context = {"concs": allconcentrations}
	return render(
   	    request,
        'index.html',
        context
    )

def login(request):
	return render(
		request,
		'login.html',
	)

@login_required
def logout(request):
	return render(
		request,
		'login.html',
	)

@login_required
def scheduler(request):
	allcourses = []
	allconcentrations = []
	cnetid = request.user.username
	courseexplanations = []
	coursedescrip = {}

	# if no current user object, make one
	if len(User.objects.filter(netid=cnetid)) > 0:
		plans = User.objects.filter(netid=cnetid).values('plans')
	# retreive user plans
	else:
		u = User(netid=cnetid)
		u.save()
		plans = []

	# for course in Course.objects.all():
	# 	coursedescrip[course.title] = course.descrip
	# 	allcourses.append(course.title_and_code())

	for conc in Concentration.objects.all():
		allconcentrations.append(conc.name)
	print (Course.objects.all_info())

	info = {"plans": plans, "courses": Course.objects.all_info(), "conclist": allconcentrations}


	return render(
		request,
		'schedule.html',
		info
	)

def sampleschedules(request):
	return render(
		request,
		'sampleschedules.html',
	)
def aas(request):
	return render(
		request,
		'aas.html',
	)