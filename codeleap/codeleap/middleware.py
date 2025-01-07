from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict

class PythonObjectToJSONResponseMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):   
        response = self.get_response(request)

        if isinstance(response, HttpResponse):
            return response

        if isinstance(response, (ReturnList, ReturnDict)):
            response = Response(response)

        elif not isinstance(response, Response):
            response = Response(response)

        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}

        response._is_rendered = False 
        response.render()                

        return response