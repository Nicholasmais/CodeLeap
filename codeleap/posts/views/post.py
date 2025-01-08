from rest_framework.views import APIView
from ..models.post import Post
from ..serializers.post_serializer import PostSerializer
from rest_framework.response import Response

class PostView(APIView):
    def get(self, request, pk = None):
        if pk:
            post = Post.objects.filter(id = pk).first()
            if not post:
                 return Response({'erro':f'Post not found.'}, 404)
            
            post_serializer = PostSerializer(post)
            return Response(post_serializer.data)
        
        posts = Post.objects.all()
        posts_serializer = PostSerializer(posts, many = True)
        return Response(posts_serializer.data)

    def post(self, request):
        if Post.objects.filter(username = request.data.get("username", None)):
            return Response({'erro':f'Username {request.data["username"]} duplicated.'}, 409)
        
        obj_to_save = PostSerializer(data = request.data)
        if obj_to_save.is_valid():
            created_post = obj_to_save.save()
            return Response(PostSerializer(created_post).data, 201)
      
        erros_messages = " ".join([err for err_list in obj_to_save.errors.values() for err in err_list])

        return Response({'erro':erros_messages}, 400)    
    
    def delete(self, request, pk = None):
        if not pk or not Post.objects.filter(id = pk).exists():
            return Response({'erro':f'Post not found.'}, 404)
                        
        post = Post.objects.get(id = pk)
        post.delete()
        
        return Response({}, 204)

    def patch(self, request, pk = None):
        if not pk or not Post.objects.filter(id = pk).exists():
            return Response({'erro':f'Post not found.'}, 404)
                        
        post = Post.objects.get(id = pk)
        new_post = request.data
                                
        if "id" in new_post:
            del new_post["id"]        
        if "username" in new_post:
            del new_post["username"]        
        if "created_datetime" in new_post:
            del new_post["created_datetime"]

        new_post_serializer = PostSerializer(post, new_post, partial = True)
               
        if new_post_serializer.is_valid():
            created_post = new_post_serializer.save()
            return Response(PostSerializer(created_post).data)

        erros_messages = " ".join([err for err_list in new_post_serializer.errors.values() for err in err_list])

        return Response({'erro':erros_messages}, 400)    

    