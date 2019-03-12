from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.db.models import Q

from .models import data
import logging
import json
import csv
import os
import sys
import elasticsearch 

init_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(init_path)

##########################################################
#Global Variables
##########################################################
# Get an instance of a logger
logger = logging.getLogger(__name__)

ES_URL ='http://localhost:9200/'
import elasticsearch
import pandas as pd
class pushdata(View):
    res={}
    def get(self,request):
        res={}
        try:
            params = request.GET
            path =  params.get('path')
            index =  params.get('index')
            csvfile=open(path,'r')
            reader = csv.DictReader(csvfile)
            dict_list =[]
            for row in reader:
                dict_list.append(row)
            es=elasticsearch.Elasticsearch(ES_URL)
            for ob in dict_list:
                es.index(
                        index =index,
                        doc_type ='Data',
                        body =ob
                        )
            status = "Success"
        except Exception as e:
            status = "Failure, " + str(e)
        
        res["status"] = status
        return HttpResponse(json.dumps(res))


#API: UI
#Return: 
#URL: http://localhost:8000/BDA/ES/BDA.html
##########################################################
def insertdata(request):
    template = loader.get_template("insertdata.html")
    return HttpResponse(template.render())
