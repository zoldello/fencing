============
Contributing
============

No contribution accepted. This is work to demonstrate Philip Adenekan programming skills.


Report Bugs
~~~~~~~~~~~

Report bugs at Philip at: greenish_green@yahoo.com

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/zoldello/fencing/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `fencing` for local development.

1. Get code from Philip Adenekan

2. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv fencing
    $ cd fencing/
    $ python setup.py develop


2. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ flake8 fencing tests
    $ python setup.py test or py.test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

Tips
----

To run a subset of tests::

$ py.test tests.test_fencing
