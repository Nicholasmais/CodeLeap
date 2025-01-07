from rest_framework.views import APIView
from ..models.career import Career
from ..serializers.career_serializer import CareerSerializer
from rest_framework.response import Response

class CareerView(APIView):
    def get(self, request, pk = None):
        if pk:
            career = Career.objects.filter(id = pk).first()
            if not career:
                 return Response({'erro':f'Career not found.'}, 404)
            
            career_serializer = CareerSerializer(career)
            return Response(career_serializer.data)
        
        careers = Career.objects.all()
        careers_serializer = CareerSerializer(careers, many = True)
        return Response(careers_serializer.data)

    def post(self, request):
        if Career.objects.filter(username = request.data.get("username", None)):
            return Response({'erro':f'Username {request.data["username"]} duplicated.'}, 409)
        
        obj_to_save = CareerSerializer(data = request.data)
        if obj_to_save.is_valid():
            created_career = obj_to_save.save()
            return Response(CareerSerializer(created_career).data)
      
        erros_messages = " ".join([err for err_list in obj_to_save.errors.values() for err in err_list])

        return Response({'erro':erros_messages}, 400)    
    
    def delete(self, request, pk = None):
        if not pk or not Career.objects.filter(id = pk).exists():
            return Response({'erro':f'Career not found.'}, 404)
                        
        career = Career.objects.get(id = pk)
        career.delete()
        
        return Response({}, 204)

    def patch(self, request, pk = None):
        if not pk or not Career.objects.filter(id = pk).exists():
            return Response({'erro':f'Career not found.'}, 404)
                        
        career = Career.objects.get(id = pk)
        new_career = request.data
                                
        if "id" in new_career:
            del new_career["id"]        
        if "username" in new_career:
            del new_career["username"]        
        if "created_datetime" in new_career:
            del new_career["created_datetime"]

        new_career_serializer = CareerSerializer(career, new_career, partial = True)
               
        if new_career_serializer.is_valid():
            created_career = new_career_serializer.save()
            return Response(CareerSerializer(created_career).data)

        erros_messages = " ".join([err for err_list in new_career_serializer.errors.values() for err in err_list])

        return Response({'erro':erros_messages}, 400)    

    