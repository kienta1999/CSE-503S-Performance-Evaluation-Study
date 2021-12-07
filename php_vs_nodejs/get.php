<?php
    ini_set("session.cookie_httponly", 1);
    header("Content-Type: application/json");

    echo json_encode(array(
        "success" => true,
        "first_name" => "Anh",
        "last_name" => "Le"
    ));

    exit;
?>
