
from .serializers import UserSerializer,RegisterSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import UserSerializer
from .serializers import registerSerializer ,RecepieSerializer,InstructionSerilaizer, IngridientSerilaizer
from rest_framework import viewsets
from .models import Recepie,Ingredient,Instruction
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

#######################################################
######## 

class RegisterView(generics.CreateAPIView):
    serializer_class = registerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Prepare response data
        response_data = {
            'refresh': refresh_token,
            'access': access_token,
        }
        
        # Optionally add user details
        user_serializer = UserSerializer(user)
        response_data.update(user_serializer.data)

        return Response(response_data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)




# ##################################################
# ########recepie view ###### using viewset

# class recepieview(viewsets.ViewSet):
#     # authentication_classes=[jwt]
#     permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]
#     # permission_classes = [IsOwnerOrReadOnly]
#     # queryset=recepie.objects.all()
#     # serializer_class=recepieSerializer
#     def list(self,request):
#         recepies=Recepie.objects.all()
#         serializer=RecepieSerializer(recepies,many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer=RecepieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self,request,pk=None):
#         recipe = get_object_or_404(Recepie, pk=pk)
#         self.check_object_permissions(request, recipe)
#         serializer=RecepieSerializer(recipe,data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self,request,pk=None):
#         recipe=get_object_or_404(Recepie,pk=pk)
#         self.check_object_permissions(request, recipe)
#         recipe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def retrieve(self,request,pk=None):
#         recipe=get_object_or_404(Recepie,pk=pk)
#         serializer=RecepieSerializer(recipe)
#         return Response(serializer.data)
    


########################################################################


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngridientSerilaizer
    permission_classes = [IsAuthenticatedOrReadOnly]


class InstructionViewSet(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerilaizer
    permission_classes = [IsAuthenticatedOrReadOnly]



from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import RecipeFilter

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recepie.objects.all()
    serializer_class = RecepieSerializer

    # Add filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RecipeFilter

    # Specify fields for searching
    search_fields = ['name', 'desc', 'ingredients__ingrideint_name']

    # Specify fields for ordering
    ordering_fields = ['name', 'desc', 'user', 'created_at']
    ordering = ['name']  # Default ordering
