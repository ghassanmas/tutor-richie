Richie plugin for `Tutor <https://docs.tutor.overhang.io>`__
============================================================

.. TODO add some information here

Installation
------------

::

    pip install tutor-richie

Usage
-----

::

    tutor plugins enable richie
    tutor local quickstart

Create superuser::

    tutor local run richie ./sandbox/manage.py createsuperuser

Create demo site::

    # WARNING: do not attempt this in production!
    tutor local run richie ./sandbox/manage.py create_demo_site --force

Development
-----------

Bind-mount volume::

    tutor dev bindmount richie /app/richie

Then, run a development server::

    tutor dev runserver --volume=/app/richie richie

License
-------

This software is licensed under the terms of the `AGPLv3 <https://www.gnu.org/licenses/agpl-3.0.en.html>`__.
