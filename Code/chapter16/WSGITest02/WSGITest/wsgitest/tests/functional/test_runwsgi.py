from wsgitest.tests import *

class TestRunwsgiController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='runwsgi', action='index'))
        # Test response...
