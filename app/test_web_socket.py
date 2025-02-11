import json
from channels.testing import WebsocketCommunicator
from app.consumers import UserConsumer
from config.asgi import application
from django.test import TestCase

class WebSocketTestCase(TestCase):
    async def test_user_notification(self):
        communicator = WebsocketCommunicator(application, "ws/users/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        message = {
            'message': 'User testuser created'
        }
        await communicator.send_json_to(message)

        response = await communicator.receive_json_from()
        self.assertEqual(response, {'message': 'User testuser created'})
        
        await communicator.disconnect()
