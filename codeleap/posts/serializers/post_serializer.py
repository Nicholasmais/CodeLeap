from ..models.post import Post
from utils.ModelErrorHandling import CustomModelSerializer

class PostSerializer(CustomModelSerializer):
    class Meta:
        model = Post
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
