import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from stream.lib.base import BaseController, render
#from stream import model

log = logging.getLogger(__name__)

import time

class StreamingController(BaseController):

    def output(self):
        number = 0
        while 1:
            number += 1
            yield str(number)
            time.sleep(2)

