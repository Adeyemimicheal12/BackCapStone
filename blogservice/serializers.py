# from rest_framework import serializers
# from .models import BlogPost



# class BlogPostSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=BlogPost
#         fields=['id','title','content','updated_at','author','category']


# serializers.py

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'updated_at', 'category']
