from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MemberSerializer
from .models import Member


class Index(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request):
        snippets = Member.objects.all()
        serializer = MemberSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "SUCSSES"},  status=status.HTTP_201_CREATED)
        return Response({"status": "FAILED"},  status=status.HTTP_400_BAD_REQUEST)
