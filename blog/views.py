from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from blog.models import Blog, BlogCategory
from blog.serializers import BlogSerializer


class BlogView(ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.watches += 1
        obj.save()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def category_ids(self, request, pk=None):
        try:
            blog_category = BlogCategory.objects.get(pk=pk)
        except BlogCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        blogs = Blog.objects.filter(category=blog_category)

        serializer = BlogSerializer(blogs, many=True, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)
