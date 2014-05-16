<?php

$f3=require('lib/base.php');

$f3->config('etc/config.ini');

$f3->set('AUTOLOAD','api/; web/;');

$f3->route('GET /api/item/recent', 'Item->recent');
$f3->route('POST /api/item', 'Item->new_item');
$f3->route('POST /api/blog', 'Item->blog');
$f3->route('GET /api/token', 'Item->token');

$f3->route('GET /', function($f3) {
  $f3->set('web_base', $f3->get('WEB_BASE'));
  $f3->set('link', $_REQUEST['link']);
  $f3->set('title', $_REQUEST['title']);
  $f3->set('name', $_REQUEST['name']);
  
  $view=new View;
  echo $view->render('web/add.html');
});

$f3->route('GET /add', function($f3) {
  $f3->set('web_base', $f3->get('WEB_BASE'));
  $f3->set('link', $_REQUEST['link']);
  $f3->set('title', $_REQUEST['title']);
  $f3->set('name', $_REQUEST['name']);

  $view=new View;
  echo $view->render('web/add.html');
});

$f3->run();

?>