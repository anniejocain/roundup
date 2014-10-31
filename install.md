Installing Roundup
=====

Roundup is a Python application built on the [Django](https://www.djangoproject.com/) web framework.

Here's a rough set of notes to help you setup your environment so that you can develop and deploy Roundup.

### Python, Django, and modules

To develop Roundup, install Python and the Python package manager, `pip`.

The required modules are found in `requirements.txt. Install them using `pip`:

    $ pip install -r requirements.txt

If you're running OS X Mountain Lion, you may need to add the MySQL binaries 
to your PATH:

    $ export PATH=$PATH:/usr/local/mysql/bin

If you're running Ubuntu or Linux distro you might need to install mysql_config using:

    $ apt-get install libmysqlclient-dev

Sometimes LXML can be a little difficult to install. Using static dependencies can help (especially if you're using OS X).

    $ STATIC_DEPS=true pip install lxml


### Database installation

You'll need a Django friendly database. SQLite is not currently supported. We recommend MySQL.

If you want to use MySQL, something like the following can be used to create a new user and a new database:

	mysql -u root -psomepasshere
	mysql> create database roundup character set utf8; grant all on roundup.* to roundup@'localhost' identified by 'roundup';
	mysql -u roundup -proundup roundup

### Settings

Roundup settings are held in the settings file. Copy the example and fill in as you see fit.

    cp ./settings.example.py ./settings.py

Set a `SECRET_KEY` in `settings.py` and update the database and logging related values if the defaults don't fit your needs.

### Create your tables and fire up Django

You should have the pieces in place. Let's create the tables in your database using the syncdb command:

    $ python manage.py syncdb --noinput

Then apply South migrations:

    $ python manage.py migrate

If you want to play with the admin views, load the user and group data fixtures:

    $ python manage.py loaddata fixtures/users.json fixtures/groups.json

The password for all test users is "pass".

### Run the server

Toss in a WSGI config and wire it to your webserver, or use the built-in Django webserver and you should be ready to roll:

    $ python manage.py runserver