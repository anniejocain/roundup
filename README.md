roundup
======

Rounding up the team's links for a regular blog post

## Install

### MySQL

Create a new user and a new database:

	mysql -u root -psomepasshere
	mysql> create database roundup character set utf8; grant all on roundup.* to roundup@'localhost' identified by 'roundup';

You likely want your DB to have one table that looks like this:

	CREATE TABLE `roundup` (
	  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	  `link` varchar(255) DEFAULT NULL,
	  `title` varchar(255) DEFAULT NULL,
	  `description` varchar(255) DEFAULT NULL,
	  `creator` varchar(255) DEFAULT NULL,
	  `added` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	  `posted` tinyint(1) DEFAULT '0',
	  `image_name` varchar(255) DEFAULT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=MyISAM AUTO_INCREMENT=186 DEFAULT CHARSET=latin1;

### WordPress Developer credentials

If you don't already have a wordpress.com account, sign up for a one at http://wordpress.com/

Use that account to create a new application at https://developer.wordpress.com/apps/new/

The 'Website URL' is http://yourdomain.com/roundup and the 'Redirect URL' is http://yourdomain/roundup/api/token

Once you have created an application, visit https://developer.wordpress.com/apps/ to get the 'Client ID' and 'Client Secret'

### Get blog ID and access token

Use the previous info and visit the following.

http://yourdomain.com/roundup/api/token?WP_REDIRECT=YOUR_WP_REDIRECT&WP_CLIENT_SECRET=YOUR_WP_CLIENT_SECRET&WP_CLIENT_ID=YOUR_WP_CLIENT_ID

This will display your access key and blog ID

### Settings

Roundup settings are held in the settings module file. Copy the example and fill in as you see fit.  

Use the 'Client ID' and 'Client Secret' previously acquired as 'WP_CLIENT_ID' and 'WP_CLIENT_SECRET'

Use the 'access key' and 'blog ID' as 'WP_TOKEN' and 'WP_BLOG'

    cd etc; cp ./config.sample.ini ./config.sample.ini

### PHP GD

We use the PHP GD library to resize our screen captures. If you're on Redhat, you might install GD using a command like the following.

    yum install php-gd

## License

Dual licensed under the MIT license (below) and [GPL license](http://www.gnu.org/licenses/gpl-3.0.html).

<small>
MIT License

Copyright (c) 2012 The Harvard Library Innovation Lab

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
</small>
