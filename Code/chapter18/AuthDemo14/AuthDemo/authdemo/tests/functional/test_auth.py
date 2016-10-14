from authdemo.tests import *

class TestAuthController(TestController):

    def test_index(self):
        response = self.app.get(
            url(controller='auth', action='public'),
            # Not needed when using the authkit.setup.fakeuser option
            # extra_environ={'REMOTE_USER':'visitor'}
        )
        # Test response...
        assert "you are signed in" in response.body

