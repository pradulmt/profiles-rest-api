from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """
    Test APIView
    """
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            '1',
            '2',
            '3'
        ]
        return Response({'message': 'done!', 'an_apiview': an_apiview})

