from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
import base64


class Mask(APIView):
    """
    Checks if a person is wearing mask or not.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            has_mask = True
            img_data = self.decodeJSON(request.data)
            has_mask = self.check_mask(img_data)
            return Response(data=has_mask, status=status.HTTP_200_OK)
        except:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)

    def decodeJSON(self, data):
        with open("media/abhi.jpeg", "wb") as fh:
            fh.write(base64.decodebytes(bytes(data.get('img'), 'utf-8')))
        return True

    def check_mask(self, img_data):
        "Takes the image and predict using ML model"
        return True
