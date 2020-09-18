from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
from image_detect import checkmask
from PIL import Image
from io import BytesIO
import base64


class Mask(APIView):
    """
    Checks if a person is wearing mask or not.
    """
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        pass

    def post(self, request):
        try:
            im = Image.open(BytesIO(base64.b64decode(request.data.get('img'))))
            has_mask = checkmask(im)
            print("has_mask:-", has_mask)
            return Response(data=has_mask, status=status.HTTP_200_OK)
        except:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
