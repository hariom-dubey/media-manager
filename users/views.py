from django.shortcuts import render
from django.http import HttpResponse
import json

def details(request):
    return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')
