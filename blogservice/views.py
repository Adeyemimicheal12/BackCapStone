from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog_post(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_blog_post(request, pk):
    try:
        blog_post = BlogPost.objects.get(pk=pk, author=request.user)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BlogPostSerializer(blog_post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_blog_post(request, pk):
    try:
        blog_post = BlogPost.objects.get(pk=pk, author=request.user)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    blog_post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
