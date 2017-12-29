# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .serializers import TeamlistSerializer
from .models import Teamlist

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = Teamlist.objects.all()
    serializer_class = TeamlistSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teamlist.objects.all()
    serializer_class = TeamlistSerializer
