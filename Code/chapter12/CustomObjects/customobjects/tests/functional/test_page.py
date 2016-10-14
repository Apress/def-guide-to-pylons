from customobjects.tests import *

class TestPageController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='page', action='index'))
        # Test response...

    def test_cache(self):
        response = self.app.get(url(controller='page', action='view', id='1'))
        assert hasattr(response, 'cache') is True

