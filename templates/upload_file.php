<?php
  define ('SITE_ROOT', realpath(dirname(__FILE__)));
  echo realpath(dirname(__FILE__)); 						#/var/www/html/4001Y/phpworkshop
  echo '<br>';
  echo exec('whoami');										#apache
  $allowedExts = array("gif", "jpeg", "jpg", "png");
  $temp = explode(".", $_FILES["file"]["name"]);
  $extension = end($temp);  
  $extension = strtolower($extension);
  $uploadholder = realpath(dirname(__FILE__)) . "/uploadarea";
  if ((($_FILES["file"]["type"] == "image/gif")
      || ($_FILES["file"]["type"] == "image/jpeg")
      || ($_FILES["file"]["type"] == "image/jpg")
      || ($_FILES["file"]["type"] == "image/pjpeg")
      || ($_FILES["file"]["type"] == "image/x-png")
      || ($_FILES["file"]["type"] == "image/png"))
      && ($_FILES["file"]["size"] < 500000)
      && in_array($extension, $allowedExts)) {
            if ($_FILES["file"]["error"] > 0) {
                        echo "Return Code: " . $_FILES["file"]["error"] . "<br>";
            } else {
                        if (file_exists(SITE_ROOT . "/uploadarea/" . $_FILES["file"]["name"])) {
                                    echo '<p><hr>';
                                    echo $_FILES["file"]["name"] . " already exists. ";
                                    echo '<p><hr>';
                                    $petpic = "NULL";
                        } else {
                                    # move_uploaded_file(SITE_ROOT . "/index2.php", SITE_ROOT . "/uploadarea/" . $_FILES["file"]["name"]);
                                    echo '<br>';
                                    echo $_FILES["file"]["tmp_name"]; #/var/www/html/4001Y/phpworkshop/index2.php
                                    echo '<br>';
                                    echo SITE_ROOT . "/uploadarea/" . $_FILES["file"]["name"]; #/var/www/html/4001Y/phpworkshop/uploadarea/dog-puppy.jpeg
                                    if (file_exists($_FILES["file"]["tmp_name"]))
                                    {
                                    echo '<br> file exists';
                                    }
                                    else
                                    {
                                    echo '<br> file does not exist';
                                    } 
                                    move_uploaded_file($_FILES["file"]["tmp_name"], SITE_ROOT . "/uploadarea/" . $_FILES["file"]["name"]);
                                    
                                    #new temp folder unique name
                                    $petpic = SITE_ROOT . "/uploadarea/" . $_FILES["file"]["name"];
                        } // end of else
            } // end of else
     } else {
            echo "Invalid file";
    } //end of else
?>
