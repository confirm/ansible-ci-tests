Contribution
============

Merge Requests
--------------

We would be happy to get new contributors. Feel free to open issues and send us merge requests.

Branches
--------

Please note that we use `Vincent Driessen's gitflow model <http://nvie.com/posts/a-successful-git-branching-model/>`_, so make sure you create proper feature branches.

All **branches must be properly named**, which means:

* ``develop`` is the bleeding-edge **development branch**
* ``master`` is the latest **stable branch**
* ``hotfix-*`` branches are **hotfix branches**
* ``release-*`` branches are **release branches**

**Feature branches** have no fix naming scheme, though their name should describe the feature accordingly.

Tags
----

We're using **semantic versioning**, which means:

* version **tags** are named ``v{MAJOR}.{MINOR}.{BUGFIX}``
* **release branches** are named ``release-{MAJOR}.{MINOR}``

Commit messages
---------------

Also make sure you use **proper commit messages** and **prefix** them with:

* ``FEATURE: Added new foobar feature``
* ``BUGFIX: Fixed foobar bug``
* ``DOCS: Updated the documentation for foobar``
* ``REFACTOR: Refactored code of foobar`` *which didn't affect the meaning of the code itself*

If there's an issue available (especially for bugs) make sure you mention the **issue number** it in the git commit message as well:

* ``FEATURE #42: Added new foobar feature``
* ``BUGFIX #42: Fixed foobar bug``

Creating a new release
----------------------

To create a new *ansibleci* release make sure the new version meets the following requirements:

* a **release branch** or a **hotfix branch** is existing
* everything is **checked in**
* all **classes and methods are described / documented**
* all **tests are documented** in `docs/built-in-tests.rst <https://github.com/confirm/ansibleci/blob/develop/docs/built-in-tests.rst>`_
* the new release is **tested properly**
* the PyPI `setup.py script <https://github.com/confirm/ansibleci/blob/develop/setup.py>`_ is updated with the **new targeted version**
* the docs `conf.py script <https://github.com/confirm/ansibleci/blob/develop/docs/conf.py>`_ is updated with the **new targeted version**

To test the `docs <http://ansibleci.readthedocs.org/>`_ you can either let them build on `Read the Docs <https://readthedocs.org/dashboard/ansibleci/versions/>`_ or build them locally:

.. code-block:: bash

    pip install sphinx
    cd docs/
    make html

Then create a new *ansibleci* distribution and upload it to the `test PyPI server <https://testpypi.python.org/pypi/ansibleci/>`_:

.. code-block:: bash

    ./setup.py sdist upload -r https://testpypi.python.org/pypi

Test the new package version by installing it via pip:

.. code-block:: bash

    pip install -i https://testpypi.python.org/pypi ansibleci=={version}

More about PyPI packaging can be found on `packaging.python.org <https://packaging.python.org/en/latest/distributing/#uploading-your-project-to-pypi>`_ and `diveinto.org <http://www.diveinto.org/python3/packaging.html>`_.
The basic usage of the test PyPI server can be found in `TestPyPI on wiki.python.org <https://wiki.python.org/moin/TestPyPI>`_.

If everything worked properly, create the new git tag / release and upload the package to the `live PyPI server <https://pypi.python.org/pypi/ansibleci/>`_:

.. code-block:: bash

    # Merge release branch into master.
    git checkout master
    git merge --no-ff release-{MAJOR}.{MINOR}   # or hotfix-*
    git push

    # Delete release branch.
    git branch -d release-{MAJOR}.{MINOR}       # or hotfix-*
    git push -u origin :release-{MAJOR}.{MINOR} # or hotfix-*

    # Tag release.
    git tag -a [-s -u {GPG key ID} v{MAJOR}.{MINOR}.{BUGFIX}]
    git push -u origin v{MAJOR}.{MINOR}.{BUGFIX}

    # Create and upload new PyPI release.
    ./setup.py sdist upload

The `docs <http://ansibleci.readthedocs.org/>`_ will be generated automatically.
