import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from formdemo.lib.base import BaseController, render
#from formdemo import model

log = logging.getLogger(__name__)

import os
from pylons import config
import shutil
from mimetypes import guess_type

class UploadController(BaseController):

    def index(self):
        return render('/uploadform.html')

    def upload(self):
        myfile = request.POST['myfile']
        permanent_file = open(
            os.path.join(
                config['app_conf']['permanent_store'],
                myfile.filename.lstrip(os.sep)
            ),
            'wb'
        )
        shutil.copyfileobj(myfile.file, permanent_file)
        myfile.file.close()
        permanent_file.close()
        return 'Successfully uploaded: %s, description: %s' % (
            myfile.filename,
            request.POST['description']
        )

    def download(self):
        requested_filename = request.params['requested_filename']
        filename = os.path.join(
            config['app_conf']['permanent_store'],
            requested_filename.lstrip(os.sep)
        )
        if not os.path.exists(filename):
            return 'No such file'
        permanent_file = open(filename, 'rb')
        data = permanent_file.read()
        permanent_file.close()
        response.content_type = guess_type(filename)[0] or 'text/plain'
        response.headers['Content-Disposition'] = 'attachment; filename="%s"'%(
            requested_filename
        )
        return data
    
    
