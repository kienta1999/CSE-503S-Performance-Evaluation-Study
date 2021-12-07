<?php
    header("Content-Type: application/json");
    $json_str = file_get_contents('php://input');
    $json_obj = json_decode($json_str, true);

    $first_name = $json_obj['first_name'];
    $last_name = $json_obj['last_name'];

    echo json_encode(array(
        "success" => true,
        "first_name" => $first_name,
        "last_name" => $last_name
    ));
    $stmt->close();
?>