document.addEventListener("DOMContentLoaded", function(evt){
    console.log("Document was successfully loaded");
    loadData();
});

function loadData(){
    const url = "./data.json";
    console.log("Attempting to retrieve data from: " + url);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            console.log("Received data");
            let data = JSON.parse(xhttp.responseText); // convert data to JSON
            console.log("Received %s records", data.length);
            // let str = buildListFromData(data);
            // document.getElementById("list").innerHTML = str;
            let str = buildTableFromData(data);
            document.getElementById("tbl").innerHTML = str;
        }
    };
    xhttp.open("GET", url, true);   // Initial Call, defines the URI being accessed
    xhttp.send();
}

function buildTableFromData (data) {
    var table = document.getElementById("tbl");
    var line = "";

    data.forEach(el => {
        line += "<tr>";
        line += "<td>"+ el.fname + "</td>";
        line += "<td>" + el.lname + "</td>";
        line += "</tr>"
    })
    
    return line;
}