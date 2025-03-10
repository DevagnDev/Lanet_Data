from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer
import jwt,datetime

# Create your views here.

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise Exception('User not found')
        
        if not user.check_password(password):
            raise Exception('Wrong password')
        
        payload = {
            'id': user.id,
            # 'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload,
                           'secret',
                           algorithm='HS256').decode('utf-8')
        
        response=Response()
        response.set_cookie(key='jwt',value=token, httponly=True)  # setting a cookie in the response header
        response.data= {
            'jwt': token
        }

        return response
        # return Response({'token': user.get_token()})


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise Exception('Unauthenticated token')
        
        try:
            payload = jwt.decode(token,'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise Exception('Token expired')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

class LogoutView(APIView):
    def post(self, request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message': 'success'
        }
        return response