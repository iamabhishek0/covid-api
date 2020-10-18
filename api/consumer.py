import base64
import io
import json
import time

from PIL import Image
from channels.generic.websocket import WebsocketConsumer
from image_detect import checkmask


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("[INFO] Web Client Connected")

    def disconnect(self, close_code):
        print("[INFO] Web Client Disconnected")

    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        #
        # print(type(text_data))
        # start = time.time()
        print("[INFO] Data Receieved :")
        self.send(text_data=json.dumps({
            'message': strtonumpy(text_data)
        }))
        # end = time.time()
        # print("total Execution Time:", end - start)


def strtonumpy(s):
    img = Image.open(io.BytesIO(base64.b64decode(s[22:]))).convert('RGB')
    return checkmask(img)
