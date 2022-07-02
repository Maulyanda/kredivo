from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse

import json
import datetime
import requests

# Create your views here.

class Redis(APIView):

    def get(self, request):

        # Command/Terminal : loadtest -n 100 -k {{base_url}}/movie/tes_redis
        
        api_key = "4e9ee3915931c54de5866e3c01d213e2"

        # GET DATA
        list_id = "8208948"

        lists = requests.get('https://api.themoviedb.org/4/list/'+list_id+'?api_key='+api_key)

        return HttpResponse(
            lists,
            content_type="application/json"
        )

# Read all list from user list and all movie list
class Lists(APIView):

    def get(self, request):
        
        api_key = "4e9ee3915931c54de5866e3c01d213e2"

        list_id = self.request.query_params.get('pk')
        lists = requests.get('https://api.themoviedb.org/4/list/'+list_id+'?api_key='+api_key)

        return HttpResponse(
            lists,
            content_type="application/json"
        )

# Create Watch list (user can add to their watch list)
class CreateLists(APIView):

    def post(self, request):

        access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzY29wZXMiOlsiYXBpX3JlYWQiLCJhcGlfd3JpdGUiXSwidmVyc2lvbiI6MSwibmJmIjoxNjU2Nzc1OTQ2LCJzdWIiOiI2MmJmYjQyNTZhMzAwYjAwNGJhYjE1YTQiLCJhdWQiOiI0ZTllZTM5MTU5MzFjNTRkZTU4NjZlM2MwMWQyMTNlMiIsImp0aSI6IjQ1NjEwNjUifQ.FPpus4ZfESsfqv9M-JMFB7BoNNumvORG0pPIaJTFPGw"
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+access_token,
        }

        payload = request.data

        res = requests.post('https://api.themoviedb.org/4/list', headers=headers, data=json.dumps(payload))
        data = res.json()
        return Response({"status": "success", "data": data})

# Update watch list (user can edit note from each watch list)
class UpdateLists(APIView):
    
    def put(self, request):

        access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzY29wZXMiOlsiYXBpX3JlYWQiLCJhcGlfd3JpdGUiXSwidmVyc2lvbiI6MSwibmJmIjoxNjU2Nzc1OTQ2LCJzdWIiOiI2MmJmYjQyNTZhMzAwYjAwNGJhYjE1YTQiLCJhdWQiOiI0ZTllZTM5MTU5MzFjNTRkZTU4NjZlM2MwMWQyMTNlMiIsImp0aSI6IjQ1NjEwNjUifQ.FPpus4ZfESsfqv9M-JMFB7BoNNumvORG0pPIaJTFPGw"
    
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+access_token,
        }

        # get params 
        list_id = self.request.query_params.get('pk')

        # get body
        payload = request.data

        res = requests.put('https://api.themoviedb.org/4/list/'+list_id, headers=headers, data=json.dumps(payload))
        data = res.json()
        return Response({"status": "success", "data": data})

# Delete watch list
class DeleteLists(APIView):
    
    def delete(self, request):

        access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzY29wZXMiOlsiYXBpX3JlYWQiLCJhcGlfd3JpdGUiXSwidmVyc2lvbiI6MSwibmJmIjoxNjU2Nzc1OTQ2LCJzdWIiOiI2MmJmYjQyNTZhMzAwYjAwNGJhYjE1YTQiLCJhdWQiOiI0ZTllZTM5MTU5MzFjNTRkZTU4NjZlM2MwMWQyMTNlMiIsImp0aSI6IjQ1NjEwNjUifQ.FPpus4ZfESsfqv9M-JMFB7BoNNumvORG0pPIaJTFPGw"
    
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+access_token,
        }

        # get params 
        list_id = self.request.query_params.get('pk')

        res = requests.delete('https://api.themoviedb.org/4/list/'+list_id, headers=headers)
        data = res.json()
        return Response({"status": "success", "data": data})
