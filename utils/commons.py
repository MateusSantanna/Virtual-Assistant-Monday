from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import Request, Response, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

# Views
class CommonInfoView(CreateAPIView):
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def create(self, request: Request, *args, **kwargs) -> Response:
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"detail": "This user already has this type of information registered. Try to update it."}, 
                status.HTTP_409_CONFLICT
            )


class CommonInfoDetailView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user)
    
    def get_object(self):
        return get_object_or_404(self.get_queryset(), user=self.request.user)

# ============================================
