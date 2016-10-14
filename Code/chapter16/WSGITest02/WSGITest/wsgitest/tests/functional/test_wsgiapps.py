from wsgitest.tests import *

class TestWsgiappsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='wsgiapps', action='index'))
        # Test response...
