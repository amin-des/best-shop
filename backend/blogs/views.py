from rest_framework import generics, permissions
from .models import UsersPosts
from .serializers import UsersPostsSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = UsersPosts.objects.filter(is_delete=False, is_published=True)
    serializer_class = UsersPostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsersPosts.objects.filter(is_delete=False)
    serializer_class = UsersPostsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise PermissionError("You can only update your own posts.")
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()
