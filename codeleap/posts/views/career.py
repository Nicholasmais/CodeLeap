from rest_framework.views import APIView
from ..models.career import Career
from ..serializers.career_serializer import CareerSerializer
from rest_framework.response import Response

class CareerView(APIView):
    def get(self, request):
        careers = Career.objects.all()
        careers_serializer = CareerSerializer(careers, many = True)
        return Response(careers_serializer.data)

    def post(self, request):
        if Career.objects.filter(username = request.data.get("username", None)):
            return Response({'erro':f'Username {request.data["username"]} duplicated.'}, 409)
        
        obj_to_save = CareerSerializer(data = request.data)
        if obj_to_save.is_valid():
            created_career = obj_to_save.save()
            return Response(created_career)
      
        erros_messages = " ".join([err for err_list in obj_to_save.errors.values() for err in err_list])

        return Response({'erro':erros_messages}, 400)
