<?php
$dbhost = "34.226.195.49";
$dbuser= "root";
$dbpass = "4001Y";
$dbname = "vetoffice";
$connection = mysqli_connect($dbhost, $dbuser,$dbpass,$dbname);
if (mysqli_connect_errno()) {
     die("database connection failed :" .
     mysqli_connect_error() .
     "(" . mysqli_connect_errno() . ")"
         );
    }
?>
