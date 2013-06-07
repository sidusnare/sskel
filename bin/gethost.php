#!/usr/bin/php
<?php
$url = $argv[1];
$host = parse_url($url, PHP_URL_HOST);
if (!$host) 
{
	echo $argv[1];
} else {echo $host;}
?>
