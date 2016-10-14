from authtest.tests import *

class TestHomegrownController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='homegrown', action='index'))
        # Test response...
