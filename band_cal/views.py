from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
# Create your views here.


@api_view(["POST"])
def cals(request):
    video_bitrate=int(request.POST.get("video_bit"))
    audio_bitrate=int(request.POST.get("audio_bit"))
    length_of_video=int(request.POST.get("length_of_video"))
    no_of_videos=int(request.POST.get("no_of_videos"))
    total_bitrate=((video_bitrate+audio_bitrate)*(length_of_video*60))*no_of_videos
    rate_in_gb=(total_bitrate/1024)/1024
    formated_rate_in_gb="{:.2f}".format(rate_in_gb)
    return Response({str(formated_rate_in_gb) + "GB For " +str(length_of_video*no_of_videos)+"  Minutes of Video"})
