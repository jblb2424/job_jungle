from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import urllib.request
import urllib.parse
import json
from django.http import JsonResponse
# from . import forms
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

#URLLIB request to my api endpoint to get all job listings
@csrf_exempt
def index(request):
	req_jobs= urllib.request.Request('http://localhost:8000/api/v1/jobs/')
	resp_jobs= urllib.request.urlopen(req_jobs).read().decode('utf-8')
	resp = json.loads(resp_jobs)
	return render(request, 'index.html', {"jobs" : resp} )


#Adding an ID to end of job endpoint provides detailed information on one instance
def details(request,pk):
	req_details= urllib.request.Request('http://localhost:8000/api/v1/jobs/' + pk)
	resp_details= urllib.request.urlopen(req_details).read().decode('utf-8')
	resp = json.loads(resp_details)
	print(resp)
	

	return render(request, 'detail.html', {"job" : resp})

#Checks if a search result was submitted
#Pushes the result to my search endpoint to filter results against the keywords
@csrf_exempt
def search(request):
	results = []
	resp = ''

	if request.method == 'POST':
		url = 'http://localhost:8000/api/v1/jobs/search/'
		search_input = request.POST.get("Search", "")
		print(search_input)
		search_input = search_input.replace(" ", "+")
		req_jobs= urllib.request.Request('http://localhost:8000/api/v1/jobs/search/' + search_input)
		resp_jobs= urllib.request.urlopen(req_jobs).read().decode('utf-8')
		resp = json.loads(resp_jobs)

	return render(request, 'search.html', {"jobs" : resp})



