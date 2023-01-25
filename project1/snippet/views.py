from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer


from rest_framework.parsers import JSONParser


def snippetList(request):
   

   if request.method == 'GET':
      try: 
         snippets = SnippetSerializer(Snippet.objects.all(),many=True)
         
        
         return JsonResponse(snippets.data, safe=False)
      except : 
       print('error')
       return JsonResponse(snippets.data,status=500)
   elif request.method == 'POST':
      try:
         data = JSONParser().parse(request)
         serialiser = SnippetSerializer(data)
         if serialiser.is_valid():
            serialiser.save() 
         return JsonResponse(serialiser.data, status = 201)
      except :
         return JsonResponse(KeyError.error)


