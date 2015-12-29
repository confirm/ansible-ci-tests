Writing tests
=============

A good starting point before writing your own test, is to have a look at the existing `test modules <https://github.com/confirm/ansibleci/tree/develop/ansibleci/tests>`_.

Test class
----------

You can easily write own test modules / classes by inheriting from the `ansibleci.test.Test class <https://github.com/confirm/ansibleci/blob/develop/ansibleci/test.py>`_. When you've created your own class as a subclass of ``ansibleci.test.Test`` you've access to several methods:

.. automodule:: ansibleci.test
   :members:

Marking (sub-)tests as passed or failed
---------------------------------------

To mark a test as passed or failed you can use:

.. code-block:: python

    self.passed('Test Foo passed')
    self.failed('Test Bar failed')

Accessing config params
-----------------------

To access the config params you should call ``self.get_config()``, which gives you access to the `Config instance <https://github.com/confirm/ansibleci/blob/develop/ansibleci/config.py>`_: 

.. automodule:: ansibleci.config
   :members:

For example, if you want to access the ``FOOBAR`` config parameter:

.. code-block:: python

    config = self.get_config()
    foobar = config.FOOBAR

Helper class
------------

We're providing a `Helper class <https://github.com/confirm/ansibleci/blob/develop/ansibleci/helper.py>`_ for common used methods:

.. automodule:: ansibleci.helper
   :members:

The helper instance can be accessed by ``self.get_helper()``. For example, if you want to get the roles path:

.. code-block:: python

    helper     = self.get_helper()
    roles_path = helper.get_roles_path()

Store test class / module
-------------------------

You should never store your custom tests in the existing ``ansibleci.tests`` module.

However, you can easily create a new module and store it for example in a ``tests/`` directory next to your main script (i.e. ``test.py``).
Just make sure you've an ``__init__.py`` file in your module directory.

Enable test
-----------

To run your own test make sure you add your new test module / class to the ``ENABLED_TESTS`` config list and make sure Python can import this path.
