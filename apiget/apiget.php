<html>
<head><title>Get User List</title>
</head>
<body>
<?php
        
    $config_vals = parse_ini_file("web.config");
    
    $req_data = array();
   
    $dom = new DOMDocument();
    
    // Gather data from the input form here
    
    $req_data_q = http_build_query($req_data);
    
    // ****
    if($_GET["outputMode"] == 'html') {
        $contenttype = "text/html\n";
    }
    elseif($_GET["outputMode"] == 'json') {
        $contenttype = "application/json\n";
    }
    
    // Setup HTTP options
    $req_files = array();
    $req_options = array( 'http' => array('method' => 'GET', 'content' => $req_data_q, 'header' => "Content-type" . $contenttype . "Content-tength: " . strlen($req_data_q) . "\nAuthorization: Basic " . base64_encode($config_vals["auth_creds"]) ));
    $ret_info = array();

    // ****
    
    // Initialize stream
    
    $req_stream = stream_context_create($req_options);
    $req_fileptr = fopen($config_vals["base_url"] . "?outputMode=" .$_GET["outputMode"], 'rb', false, $req_stream);

    $req_response = stream_get_contents($req_fileptr);
    $dom->loadHTML($req_response);
    
    echo $dom->saveHTML();

?>
</body>
</html>