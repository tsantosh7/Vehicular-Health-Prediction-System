from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404,HttpResponseRedirect, HttpResponse
#from mcqportal.models import Questiondetails,Users,Answers,Q1,Q2,Q3,Q4,Profile,Skills,Following,Schools,Teststarttime,testresult
from analysis.models import data
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render
import random 
import copy
from django.db.models import Count
from django.db.models import Max 
import json
import re
import datetime
from datetime import timedelta
from datetime import datetime, date, time
from django.utils import timezone
import numpy as np

def index(request):

	return  render(request,'analysis/index.html')

def dashboard(request):
	stats=data.objects.all()
	cityl=[]
	for i in stats:
		if i.city not in cityl:
			cityl.append(i.city)
	if 'city' in request.POST:
		stats=data.objects.filter(city=request.POST['city'])
		location=[]
		for i in stats:
			location.append(i.location)
		return  render(request,'analysis/pages/dashboard_l.html',{'location':location,'city':cityl})

	if 'loc' in request.POST:
		loc=request.POST['loc']
		stats=data.objects.get(location=loc)
		l=[]
		l.append(stats.q1_2010)
		l.append(stats.q2_2010)
		l.append(stats.q3_2010)
		l.append(stats.q4_2010)
		l.append(stats.q1_2011)
		l.append(stats.q2_2011)
		l.append(stats.q3_2011)
		l.append(stats.q4_2011)
		l.append(stats.q1_2012)
		l.append(stats.q2_2012)
		l.append(stats.q3_2012)
		l.append(stats.q4_2012)

		Y = np.array(l)
		pres_mat = np.reshape(Y, (3,4)).transpose()
		ds =    pres_mat.sum(axis=0)
		nor = pres_mat/np.kron(np.ones((4,1)),ds)
		con = nor.mean(axis=1)
		x1 = np.array([4, 8, 12]);
		z = np.polyfit(x1, ds, 1)
		F = con*(z[1]+16*z[0])
		F1 = np.concatenate((Y,F)).reshape(16,1)
		stats.q1_2013=F1[12][0]
		stats.q2_2013=F1[13][0]
		stats.q3_2013=F1[14][0]
		stats.q4_2013=F1[15][0]



#	print stats.city
		return  render(request,'analysis/pages/dashboard_s.html',{'data':stats,'city':cityl})
#	return  render(request,'analysis/analysis.html')


	print cityl
	return  render(request,'analysis/pages/dashboard.html',{'city':cityl})


# Create your views here.
