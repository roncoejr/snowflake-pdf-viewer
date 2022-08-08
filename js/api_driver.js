//
//
//
//
//
//
function m_apiJazzDemoGetRequests(i) {
    //
    // v_Node: Acano API node
    // v_displayMode: output format of the response [ TABLE | SELOPTS ]
    //
    //
    // m_showPendingStatus(document.getElementById("fld_URL").value);
    xmlhttp = new XMLHttpRequest;
    
    // Do some interesting work here
    // req_data = "apiNode=" + v_Node;
    // req_data += "&apiNodeName=" + v_NodeName;
    // req_data += "&fld_displayMode=" + v_displayMode;

    req_data = "outputMode="

    omode = document.getElementsByName('fld_outputMode');
    for(i = 0; i < omode.length; i++) {
        if(omode[i].checked) {
            req_data += omode[i].value;
        }
    }
 //   req_data += document.getElementsByName("fld_outputMode")[0].value
    
    // alert(req_data);
    xmlhttp.open("GET", "apiget/apiget.php"+"?"+req_data, true);
 //   xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  //  switch (v_fieldToUpdate) {
  //          case 'fld_ivrBrandingProfile':
  //              xmlhttp.onreadystatechange = m_processapiGetReadyStateChange_ivrProfiles
  //          break;
  //          case 'fld_tenant':
  //              xmlhttp.onreadystatechange = m_processapiGetReadyStateChange_tenants;
   //         break;
   //     default:
            xmlhttp.onreadystatechange = m_processapiJazzDemoGetReadyStateChange;
            
   // }
    v_fieldToUpdate = '';
    xmlhttp.send(null);
    
    // End of interesting work
    
}

function m_processapiJazzDemoGetReadyStateChange() {
    
    // alert('apiGetStateChange: gotCalled ' + xmlhttp.readyState + ': ' + v_DisplayOption + ':--- | ' + v_fieldToUpdate);
    if(xmlhttp.readyState == 4) {
        
        if(xmlhttp.status == 200) {
            // alert('apiGetStateChange: gotCalled ' + xmlhttp.status + ': ' + v_DisplayOption + ':--- | ' + v_fieldToUpdate);
            // alert('apiGetStateChange - Status 200: gotCalled ' + xmlhttp.status);
            // m_showCompletedStatus();
            // document.getElementById["btn_showCoSpaces"].style.visibility = 'visible';
            // setTimeout(location.reload(true), 3000);
        
            // alert(v_DisplayOption);
            // alert(xmlhttp.responseText);
            document.getElementById("div_userList").innerHTML = xmlhttp.responseText;
            
            
        }
    }
}


function m_apiJazzDemoPostRequests() {
    //m_showPendingStatus(document.getElementById("fld_URL").value);
    xmlhttp = new XMLHttpRequest();

    // Set the API node to be hit
    req_data = ""; 

    m_editFormElements = document.getElementById("frm_AddEdit").elements;

    // Do some interesting work here
    for(var i = 0; i < m_editFormElements.length; i++) {
        if(m_editFormElements[i].type === "text" && !(m_editFormElements[i].value === "")) {
            if(i == 0) {
                req_data = m_editFormElements[i].id;
                req_data += "=" + m_editFormElements[i].value;
            }   
            req_data += "&" + m_editFormElements[i].id + "=" + m_editFormElements[i].value;
            m_editFormElements[i].value = "";
        }   
    }   

    // req_data += "&url=" + document.getElementById("fld_URL").value + "&fld_RA=" + document.getElementById("fld_RA").value;
    // alert(req_data);

    xmlhttp.open("POST", "apipost/apipost.php", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.onreadystatechange = m_processapiJazzDemoPostReadyStateChange;
    xmlhttp.send(req_data);
    
    return true;
    
    // End of interesting work
    
}




function m_processapiJazzDemoPostReadyStateChange() {
    
    // alert('apiGetStateChange: gotCalled ' + xmlhttp.readyState + ': ' + v_DisplayOption + ':--- | ' + v_fieldToUpdate);
    if(xmlhttp.readyState == 4) {
        
        if(xmlhttp.status == 200) {
            // alert('apiGetStateChange: gotCalled ' + xmlhttp.status + ': ' + v_DisplayOption + ':--- | ' + v_fieldToUpdate);
            // alert('apiGetStateChange - Status 200: gotCalled ' + xmlhttp.status);
            // m_showCompletedStatus();
            // document.getElementById["btn_showCoSpaces"].style.visibility = 'visible';
            // setTimeout(location.reload(true), 3000);
        
            // alert(v_DisplayOption);
            // alert(xmlhttp.responseText);
            document.getElementById("div_userList").innerHTML = xmlhttp.responseText;
            
            
        }
    }
}


