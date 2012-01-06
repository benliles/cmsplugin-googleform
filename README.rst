Introduction
------------

This is a `Django CMS` plugin for embedding a Google Document Form to a page by using the form's variable formkey. 

Google Forms is part of Google's Documents application suite and automatically links a dynamic spreadsheet that updates when a form is submitted. 
For more info on how to use the form application go to http://www.google.com/google-d-s/forms/

Installation
------------

First, you must install `Django CMS` which require `Django`. For full details, see the installation 
instructions for those packages.

Install ``cmsplugin-googleform`` to your environment with a tool such as `PIP`, 
`setuptools`, or `buildout`.

Add ``cmsplugin_googleform`` to the ``INSTALLED_APPS`` list in your project's 
``settings.py`` and run the ``syncdb`` command on your ``manage.py``.

.. _Django: http://www.djangoproject.com/
.. _Django CMS: https://www.django-cms.org/
.. _PIP: http://www.pip-installer.org/
.. _setuptools: http://pypi.python.org/pypi/setuptools/
.. _buildout: http://pypi.python.org/pypi/zc.buildout/

What's Inside
-------------

When you add the plugin to a page, you will required to input a **Form key**. To find the ``formkey`` for a form, at the top of the form spreadsheet in Google Documents, go to ``Form > Embed for in webpage...``.
In the embed code, copy the string after ``formkey=`` and paste it in the cmsplugin-googleform **Form key** field.

It is recommended that you fill out the **Height** and **Width** fields for the form (though it is not required).

**Example embed code:**
``<iframe... formkey=dG9jLXJSYUY1a3NiYTRLYWs3S1F0xxxxxxx"...</iframe>``

