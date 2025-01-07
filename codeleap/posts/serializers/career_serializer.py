from ..models.career import Career
from utils.ModelErrorHandling import CustomModelSerializer

class CareerSerializer(CustomModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
        extra_kwargs = {
            "username": {
                "error_messages": {
                    "max_length": "Username must have more than 50 characters.",                    
                    "min_length": "Username must not have less than 3 characters."
                }
            },
            "title": {
                "error_messages": {
                    "max_length": "Title must have more than 50 characters.",                    
                    "min_length": "Title must not have less than 3 characters."
                }
            }
        }

    
    def create(self, validated_data):
        created_data =  Career.objects.create(**validated_data)
        return CareerSerializer(created_data).data