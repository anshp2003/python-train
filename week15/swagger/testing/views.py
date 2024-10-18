from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserListSerializer

@api_view(['GET'])
def get_users(request):
    # Ensure you're using the correct related names 'addresses' and 'phonenumbers'
    users = CustomUser.objects.prefetch_related('addresses', 'phonenumbers').all()
    serializer = UserListSerializer({"users": users})
    return Response(serializer.data)
