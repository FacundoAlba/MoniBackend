from rest_framework import viewsets, permissions
from .models import LoanRequest
from .serializers import LoanRequestSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes_by_action = {'create': [permissions.AllowAny], 'default': [permissions.IsAuthenticated]}

    def get_permissions(self):
        return [permission() for permission in self.permission_classes_by_action.get(self.action, self.permission_classes_by_action['default'])]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()