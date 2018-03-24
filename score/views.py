# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import Context
from django.template.context_processors import csrf
from django.utils import timezone
from django.views.decorators.csrf import requires_csrf_token
from score.models import Sp2011

# Create your views here.

@requires_csrf_token
def scores(request):
	args = {}
	args.update(csrf(request))

	args['scores'] = Sp2011.objects.all().distinct()

	return render(request,'scores.html',args)

def score(request,score_id):
	score1 = Sp2011.objects.filter(id=score_id)
	score1 = list(score1.values('Title'))
	score2 = Sp2011.objects.filter(Title=score1[0]['Title'])
	score3 = list(score2.values())
	return render(request,'score.html',{'score':Sp2011.objects.get(id=score_id),'score3':score3})

def search_title(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ""
	scores = Sp2011.objects.filter(Title__contains=search_text)[:10]
	
	return render_to_response('ajax_search.html',{'scores':scores})