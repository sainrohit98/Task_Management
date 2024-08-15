from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from .models import Task
from .serializers import TaskSerializer, TaskCreateUpdateSerializer, UserSerializer

class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if not username or not password or not email:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, email=email, password=password)
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id, 'email': token.user.email})

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save()

class TaskDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateUpdateSerializer

@api_view(['PATCH'])
def update_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = request.data.get('status', task.status)
    task.save()
    return Response({'status': task.status})

@api_view(['PUT'])
def add_remove_task_members(request, pk):
    task = Task.objects.get(pk=pk)
    members = request.data.get('members', [])
    users = User.objects.filter(id__in=members)
    task.members.set(users)
    return Response(TaskSerializer(task).data)

@api_view(['GET'])
def view_task_members(request, pk):
    task = Task.objects.get(pk=pk)
    members = task.members.all()
    serializer = UserSerializer(members, many=True)
    return Response(serializer.data)
