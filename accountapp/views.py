from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import authentication, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from accountapp.models import NewModel
from accountapp.serializes import NewModelSerializer, UserSerializer, UserWithoutPasswordSerializer


def hello_world_template(request):
    return render(request, 'accountapp/hello_world.html')

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "POST":
        input_data = request.data.get('input_data')
        new_model = NewModel()
        new_model.text = input_data
        new_model.save()
        serializer = NewModelSerializer(new_model)
        return Response(serializer.data)
    new_model_list = NewModel.objects.all()
    serializer = NewModelSerializer(new_model_list, many=True)
    return Response(serializer.data)

def AccountCreateTemplate(request):
    return render(request, 'accountapp/create.html')

class AccountCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

def AccountLoginTemplate(request):
    return render(request, 'accountapp/login.html')

class AccountRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserWithoutPasswordSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]