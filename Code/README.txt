++++++++++++++++++++++++++++++
The Definitive Guide to Pylons
++++++++++++++++++++++++++++++

:date: 2008-11-10
:author: James Gardner

Index to the Source Code Examples
+++++++++++++++++++++++++++++++++

I've tested every example in the book (apart from Chapters 10, 13 and 17 which
Apress reviewed on my behalf) and copied the working code at each step into the
examples you see in this index. I've also reported any problems and the
required corrections to Apress so what you see in these examples should match
exactly what is in the book. I hope you find them useful!

These 164 examples were generated with Pylons 0.9.7rc2, SQLAlchemy 0.5rc1 andi
the development versions of their required dependencies. They have been
developed in such a way that they should also work with the release versions
too but it is possible that things will change between now and when you test
the examples for yourself. If you have difficulties try comparing your version
to the version here for clues. You can do that with this command::

    $ diff -ur MyCodeDirectory YourCodeDirectory

If you still have problems visit the Pylons Book site at http://pylonsbook.com
for updates or ask on the Pylons mailing list. We have a friendly community and
I'm sure someone will be happy to help you.

All the source code is licensed under a BSD license so you can use it in your
own projects. Some of the examples also include YUI which is licensed
separately. The licenses are at the end of this file.

Chapter 1 
=========

``CGI``
    The example CGI script and config file

Chapter 2
=========

No examples.

Chapter 3
=========

``HelloWorld``
    The empty project as a starting point.

``HelloWorld-01``
    Contains the ``index.html`` file for generating Figure 3-1 and the hello
    controller ``index()`` action for testing the message and generating the HTTP
    request and response information for Figures 3-2 and 3-3.

``HelloWorld-02``
    Contains extra routes so that the application be served from ``/`` an so
    that the ``view()`` action can be tested.

``HelloWorld-03``
    Contains the code to test the counter via ``app_globals`` and the helper to
    generate the text version of the environment print out.

Chapter 4
=========

``HelloWorld-04``
    Contains the extra ``debugger()`` action to test the Pylons interactive 
    debugger.

``HelloWorld-05``
    Disabling the debugger to send an email error report. You'll need to set
    your own email address in ``development.ini`` to test this example.

Chapter 5
=========

``TemplateDemo``
    The empty template project

``TemplateDemo-01``
    Contains the simple template to generate the ``Hello Pylons Developer!`` 
    greeting shown in Figure 5-1.

``TemplateDemo-02``
    The same example, but using the updated code using the ``c`` global and
    ``strcit_c`` option.

``TempalteDemo-03``
    Same as before but updated to include a ``basic()`` action which renders
    the ``basic.html`` template with various examples of basic Mako syntax.

``TempalteDemo-04``
    Adds the improved greeting message with the current URL and the context 
    example.

``TemplateDemo-05``
    Dynamically generates the greeting based on the query string. Also includes
    a ``filters()`` action to test some of the filters.

``TemplateDemo-06``
    Uses a namespace to generate the navigation links for the ``greeting()`` 
    action and uses the body def for a greeting and time example in the
    ``greeting_and_time()`` action.

``TemplateDemo-07``
    Uses an inheritance chain to generate the template used by the 
    ``greeting()`` action.

``TemplateDemo-08``
    Uses three templates in an inheritance chain and the ``next`` namespace
    to render the navigation links when the ``greeting()`` action is called.

``TemplateDemo-09``
    Uses the ``parent`` namespace to create a customized title.

``TemplateDemo-10``
    Uses caching so that the page is only generated every 5 seconds.

``GenshiTemplateDemo``
    An empty project where Genshi was chosen as the templating language
    during generation.

Chapter 6
=========

``FormDemo``
    The empty FormDemo project

``FormDemo-01``
    Uses a base template and a form to submit an email address and display the
    submitted value.

``FormDemo-02``
    Uses an HTTP redirect to confirm the data was successfully submitted whilst
    avoiding the resubmitted data problem.

``FormDemo-03``
    Uses helpers to generate the form.

``FormDemo-04``
    File upload and download.

``FormDemo-05``
    Manual validation and error message generation.

``FormDemo-06``
    Using FormEncode to validate the form.

``FormDemo-07``
    Using HTMLFill to re-populate the form.

``FormDemo-08``
    Using the ``@validate`` decorator.

``FormExample`` 
    The empty FormExample project.

``FormExample-01``
    Repeating fields example using a reseach study theme.

Chapter 7
=========

``filesystem``
    Contains an example Pylons project using the filesystem functions, an
    interactive session similar to the one described in the book and the 
    ``size_to_human()`` helper. There are also some tests of the functionality.

``S3``
    Contains the example for uploading and downloading a file from Amazon S3 
    using ``boto``.

``example01``
    Contains the ``engine_test.py`` example which outputs ``username: foo``.

``example02``
    Adds the ``metadata_test.py`` example to output the table name and check
    that the ``page_table`` object can be obtained from the metadata. Also 
    prints the columns being used.

``example03``
    Adds an ``sqlexpression_test.py`` and ``alternative_sqlexpression_test.py``
    examples.

``sql_injection_attack.py``
    Contains code which will run the example SQL injection attack action.

``example04``
    Selection example using the ``echo=True`` argument to ``create_engine()``.

``example05``
    Using a more complex ``WHERE`` clause with ``and`` and ``like`` operators.

``example06``
    Using an ``ORDER BY`` clause.

``example07``
    Updating and deleting records.

``example08``
    Using a model and a session.

``example09``
    Using the declarative API for the model.

Chapter 8
=========

``SimpleSite01``
    Create a skeleton SimpleSite project.

``SimpleSite02``
    Remove the ``public/index.html`` file, add a page controller and create a 
    simple ``view()`` action.

``SimpleSite03``
    Adding the template structure and a simple ``view()`` template.

``Simplesite04``
    Adding the model and updating the ``websetup.py`` file to create the 
    database.

``SimpleSite05``
    Using the home page data from the database to populate the view template

``SimpleSite06``
    Updated the ``view()`` action to handle pages which don't exist. Also added
    a ``new()`` action and a ``fields.html`` template for creating and editing 
    templates. Installing FormBuild and updating ``lib/helpers.py`` and 
    ``setup.py``. Adding the ``new.html`` template and the Routes ``url_for()``
    function.

``SimpleSite07``
    Added the ``create()`` action and the ``main.css`` stylesheet so pages can 
    now be saved. Modified the base template to include the stylesheet.

``SimpleSite08``
    Implementing the ``edit()`` and ``save()`` actions and the ``edit.html``
    template.

``SimpleSite09``
    Implementing the ``list()`` action and ``list.html`` template.

``SimpleSite10``
    Adding the ``delete()`` action and updating the footer.

``SimpleSite11``
    Adding the paginator.

``SimpleSite12``
    Implementing the flash message, in the ``save()`` action the base template
    and by adding some extra styles.

Chapter 9
=========

All examples are run from an interactive Python prompt.

Chapter 10
==========

No examples.

Chapter 11
==========

``TranslateDemo01``
    An empty Pylons project with a ``hello`` controller added.

``TranslateDemo02``
    Add ``.pot`` and ``.po`` files and compile the Spanish translation to a 
    ``.mo`` file. Test the example to use ``set_lang()`` to set the language 
    to Spanish then print the localized string ``¡Hola!``.

``TranslateDemo03``
    Create French and English translations too. Use the ``set_lang()`` and 
    ``get_lang()`` functions to change which translations are used dynamically,
    print French, English and Spanish translations in the same ``multiple()`` 
    action.

``TranslateDemo04``
    Updating the message catalog with the string ``"Goodbye!"``.

``TranslateDemo05``
    Using localisation in templates with the ``hello.html`` template.

``TranslateDemo06``
    Enabling and customizing the Babel message extractors.

``TranslateDemo07``
    Setting the default language in the config file's ``[app:main]`` section
    with ``lang = fr``.

``TranslateDemo08``
    Setting the language based on the user's session and the ``__before__()``
    action.

``TranslateDemo09``
    Setting the language based on the user's session and the ``BaseController``
    ``__call__()`` method to affect every controller.

``TranslateDemo10``
    Investigating fallback languages.

``TranslateDemo11``
    Lazy translations.

``TranslateDemo12``
    Plural forms.
    
Chapter 12
==========

``test_maths01``
    Simple nose test script to test adding and subtracting.

``test_maths02``
    Alternative use of ``AssertionError``.

``test_maths03``
    Causing a test failure.

``test_maths04``
    Adding an assertion message.

``test_maths05``
    Printing debug messages to ``sys.stdout``.

``SimpleSite13``
    Adding a test for the SimpleSite page controller's ``view()`` action and 
    ammending it to include a check of the Pylons request object from the 
    ``response.req`` object. Modifying the ``test.ini`` file to include logging
    information and running the test once to see that it accidentally adds an
    extra page.

``SimpleSite14``
    Updating the ``test.ini`` file so it has its own configuration. Updating
    the ``websetup.py`` file so that when the ``test.ini`` file is run, the 
    test database tables are dropped, losing all the data so that the tests
    can be run with a fresh database.

``SimpleSite15``
    Testing the ``save()`` action. (You can also use this for the
    ``paster shell`` example.)

``CustomObjects``
    How to add custom objects to the test ``response`` object.

Chapter 13
==========

``emphasize``
    Contains a sample module and a doctest to test it.

``hello``
    Create a sample reStructuredText document and generate an HTML file from
    it.

``programatically``
    Generating HTML from reStructuredText using library calls.

``SimpleSiteDocs1``
    Creating a sphinx build and generating a set of HTML documents.

``SimpleSiteDocs2``
    Adding some sample files, updating the toctree.

``SimpleSiteDocs3``
    Adding API documentation.

``SimpleSiteDocs4``
    Autogenerating Documentation.

``SimpleSiteDocs5``
    Syntax highlighting source code.

Chapter 14
==========

``SimpleSite16``
    Using explicit routing and updating the page footer accordingly. Adding
    routes for a comment controller. Updating the ``list()`` action so the
    paginator works with the new routes. Creating a new comment controller and
    templates from the code used by the page controller and updating the
    ``fields.html``, ``view.html`` and ``list.html`` templates. At this point
    you can generate Figure 14-1 yourself.

``SimpleSite17``
    Adding a ``__before__()`` method to the comment controller. Updated the
    controller to use the ``c.page`` object created in the ``__before__()`` 
    method and modified the comment ``view.html`` template to contain Edit and
    Delete links.

``SimpleSite18``
    Adding the comment count to the page view, changing the cascade behaviour
    so that comments are deleted when pages are.

``SimpleSite19``
    Dealing with tags. Creating the new controller and updating the templates.

``SimpleSite20``
    Modifying the validators so that tags are unique, less than 20 characters 
    long and only contain alphanumerics and the space character.

``SimpleSite21``
    Loading and saving tags correctly as well as handling their deletion.

``SimpleSite22``
    Creating a navigation hierachy, updating the model, creating the nav table,
    updating ``websetup.py`` and creating a new database.

``SimpleSite23``
    Adding a nav controller and validators and adding a section controller 
    and templates. Adding nav validators and then section validators which 
    inherit them. Also adding shared fields for the section and page forms.
    At this point you can create Figure 14-6.

``SimpleSite24``
    Updating the model so that the ``Nav`` class has a 
    ``add_navigation_node()`` static method. Setting up the section controller.

``SimpleSite25``
    Setting up the page controller

``SimpleSite26``
    Changing the routing and updating the page and section controllers 
    accordingly. Create the page and section not found templates.

``SimpleSite27``
    Adding the navigation components to the templates.

``SimpleSite28``
    Adding some style.

Chapter 15
==========

``SimpleSite29``
    Add the YUI library files to the project and setting up the reset, fonts 
    and grids CSS.

``SimpleSite30``
    Adding animation.

``SimpleSite31``
    Adding Ajax with a ``.innerHTML`` replacement.

``SimpleSite32``
    Transferring the section values via JSON.

Chapter 16
==========

``WSGITest01``
    Contains a simple controller and action used in the example comparing a 
    WSGI application to a Pylons action.

``hello``
    Contains three Hello World! WSGI applications, one written as a function,
    one using the writable object from ``start_response()`` and  the other as 
    a class.

``application``
    Contains a WSGI application class with multiple methods

``WSGITest02``
    A WSGI application as a Pylons controller

``run_with_cgi``
    Contains the ``wsgi_test.py`` application to test the ``run_with_cgi()``
    server implementation.

``hello_server``
    Contains a sample served with the ``wsgiref`` module.

``middleware/enviorn.py``
    Middleware component which adds a message to the environment.

``middleware/error.py``
    Error handling middleware.

``middleware/cookie.py``
    Cookie-setting middleware.

``gzip``
    Contains the steps involved in writing a piece of middleware which alters
    the response.

``SimpleSite33``
    Adding ``GzipMiddleware`` to the SimpleSite application.

Chapter 17
==========

``entry_points``
    Loading the Pylons installer for the SimpleSite application from the entry
    point.

``SimpleSite34``
    Adding the Gzip filter app factory and entry point

``SimpleSite35``
    Using an alternative form of the filter definition. Adding a filter 
    function and entry point.

``Stream``
    An example application which demonstrates streaming from a controller.

``config``, ``deploy``, ``registry``, ``pylons``
    Further examples

Chapter 18
==========

``AuthTest01``
    Testing a private method.

``AuthTest02``
    A homegrown authentication system using Pylons' ``__before__()`` method.

``AuthDemo01``
    Triggering a sign in by returning a 401 response.

``AuthDemo02``
    Modifying the ``private()`` action to respond to the ``REMOTE_USER``
    environment variable.

``AuthDemo03``
    Testing the UserIn permission 

``AuthDemo04``
    Using the authorisation middleware.

``AuthDemo05``
    Using the ``authorized()`` function.

``AuthDemo06``
    Triggering a Sign In by returning a 401 response.

``AuthDemo07``
    Triggering a Sign In by raising a ``NotAuthenticatedError``.

``AuthDemo08``
    Protecting a whole controller with an ``@authorize`` decorator on
    ``__before__()``.

``permissions``
    Various permission objects you can create.

``AuthDemo09``
    Adding groups and roles.

``AuthDemo10``
    Setting cookie params.

``AuthDemo11``
    Using digest authentication.

``AuthDemo12``
    Disabling AuthKit in the test setup.

``AuthDemo13``
    Using an SSL certificate.

``AuthDemo14``
    Encrypted passwords.

Chapter 19
==========

``SimpleSite36``
    Add the AuthKit configuration to the config file, modify ``websetup.py``
    and protect the ``edit()`` action.

``SimpleSite37``
    Protect the ``save()`` action, create the ``lib/auth.py`` file and use the
    updated auth helpers to protect the ``edit()``, ``save()`` and ``delete()``
    actions. 

``SimpleSite38``
    Updating the page footer to hide the Edit Page link if you aren't signed
    in. Creating the account controller and templates, modifying the base 
    template to contain the username and a sign out link in the top right.

``SimpleSite39``
    Implementing a custom sign in template and testing the permissions.

``SimpleSite40``
    Implementing the rest of the permissions checks and updating the page 
    footer. Using the paster shell to customise users, modifying the error
    documents.

``SimpleSite41``
    Customising the 403 response and adding a ``signinagain()`` action

``SimpleSite42``
    Adding a WYSIWYG interface, setting up the JavaScript, using the sam
    skin theme, adding the styles.

``SimpleSite43``
    Adding metadata to ``setup.py``, configuring ``setup.cfg`` and adding the
    AuthKit options to ``config/deployment.ini_tmpl``.

``SimpleSite44``
    Remove the static files we don't need, add the license information to the
    ``README.txt`` file and to ``public/yui/2.6.0`` and register the package 
    on the cheeseshop, uploading the files.

``SimpleSiteTemplate01``
    Create a new project template.

``SimpleSiteTemplate02``
    Add the SimpleSite files. Removing the ones you don't want.

``SimpleSiteTemplate03``
    Update the project to ask for an ``sqlalchemy_url`` variable.

``SimpleSiteTemplate04``
    Replacing the variables and uploading the finished project.

Chapter 20
==========

In each of the LogTest examples, the output from running the examples can be
seen in the ``test.log``, ``server.log`` or ``application.log`` files. For
each new example I deleted the old version of the file so you can see the 
output from just that example.

``LogTest01``
    Demonstrating server and application logs with the Paste HTTP Server in
    development mode logging to a file.

``LogTest02``
    Logging at a ``ERROR`` and ``WARNING`` levels and using a numerical value
    rather than a named level.

``LogTest03``
    Variables in log messages.

``LogTest04``
    Logging from templates.

``LogTest05``
    Sending application logs to application.log by configuring a handler in
    ``development.ini`` and sending the server logs to ``server.log``. Note 
    that ``application.log`` also contains some message logged by the Paste
    HTTP Server because it is actually using Python application log system
    to log some server messages!

``LogTest06``
    Logging messages directly to the server logs with the ``wsgi.errors``
    stream.

``LogTest07``
    Using the Pylons ``WSGIErrorHandler`` to log messages to the 
    ``wsgi.errors`` stream.

``LogTest08``
    Controlling proagation in the ``[logger_logtest]`` section.

``LogTest09``
    Using an alternative logger in the configuration and watching it propagate.

``LogTest10``
    Controlling propagation via loggers - the ``debug()`` message is filtered.

``LogTest11``
    Updating the ``other_logger`` to use a ``warning()`` which is logged.

``LogTest12``
    Proving that propagated messages aren't filtered.

``LogTest13``
    Logging SQLAlchemy messages via propagation.

``LogTest14``
    Logging AuthKit messages via a handler.

``LogTest15``
    Logging AuthKit messages via a handler and using propagation.

``LogTest16``
    Generating the ``production.ini`` file.

Chapter 21
==========

``VirtualPython``
    Contains the bash script I ran to set up the virtual Python environment.

``InstallSoftware``
    Contains the patches I had to make to install the pre-release versions of 
    the software referred to in the book.

``embedding``
    Contains a ``wsgi_app.py`` example which loads the Pylons WSGI application.

License
=======

All the code (apart from YUI) is licensed under the BSD license:

Copyright (c) 2008, 3aims Ltd
All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions 
are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above 
      copyright notice, this list of conditions and the following disclaimer
      in the documentation and/or other materials provided with the 
      distribution.
    * Neither the name of the 3aims Ltd nor the names of its contributors
      may be used to endorse or promote products derived from this software
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

YUI is licensed as follows:

Copyright (c) 2008, Yahoo! Inc.
All rights reserved.

Redistribution and use of this software in source and binary forms, with or
without modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright notice, 
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the name of Yahoo! Inc. nor the names of its contributors may be 
      used to endorse or promote products derived from this software without 
      specific prior written permission of Yahoo! Inc.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

