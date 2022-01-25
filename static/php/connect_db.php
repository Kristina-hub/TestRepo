<!--  --------------------------------------- -->
<!--        Authors: Kristina Kacmarova       -->
<!--                Miranda Postma       	  -->
<!--                Ridwan Bari               -->
<!--                Winston Herold            -->
<!--       Python Version: 3.7.4              -->
<!--       Created on: 2022-01-18             -->
<!--  --------------------------------------- -->

<?php
	$dbhost = "172.31.80.128";
	$dbuser= "root";
	$dbpass = "syllabus";
	$dbname = "accounts";
	$connection = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);
	
	if (mysqli_connect_errno()) {
 		die("Error: database connection failed :" . 
 		mysqli_connect_error() . " (" . mysqli_connect_errno() . ")" );
 	} 
?>
