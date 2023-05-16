from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    # id, 비밀번호, 비밀번호 확인
    password = request.data.get('password')
    password_confirm = request.data.get('passwordConfirm')
    print(request.data)
    if password != password_confirm:
        return Response({'error':'비밀번호가 일치안해'},status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    
    # 유효성 검사
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
    #비밀번호 hash해서 저장 
    user.set_password(request.data.get('password'))
    user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)