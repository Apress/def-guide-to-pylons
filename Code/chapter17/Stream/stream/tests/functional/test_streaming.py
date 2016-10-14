from stream.tests import *

class TestStreamingController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='streaming', action='index'))
        # Test response...
