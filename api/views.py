from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.http import JsonResponse
from django.shortcuts import render
from .models import Job
from . import serializers
from django.db.models import Q

# Create your views here.


#### LIST AND POST VIEWS ####
class get_jobs(generics.ListCreateAPIView):
	queryset = Job.objects.all()
	serializer_class = serializers.JobSerializer


class search_jobs(generics.ListCreateAPIView):
	serializer_class = serializers.JobSerializer
	def get_queryset(self):
		game = self.kwargs['search']
		game = game.replace("+", " ")
		print(game)
		return Job.objects.filter(Q(title__icontains=game) | Q(location__icontains=game) | Q(company__icontains=game))



#### RETRIVE / UPDATE / DESTROY VIEWS ####
class detail_jobs(generics.RetrieveUpdateDestroyAPIView):
	queryset = Job.objects.all()
	serializer_class = serializers.JobSerializer