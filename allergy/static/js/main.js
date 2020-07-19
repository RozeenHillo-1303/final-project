$(document).ready(function(){
    $.getJSON("../static/json/Numbers.json",function(data){
     var list = document.getElementById("listjson");
             for(var i = 0; i < 7;i++){
                 var li = document.createElement("li");
                 var divcompenent = document.createElement("div");
                var name = document.createElement("div");
                var number = document.createElement("div");
                divcompenent.className = "hospital";
                name.className = "name";
                number.className = "number";
                name.appendChild(document.createTextNode('hospital name:' +data[i]["Name"]));
                number.appendChild(document.createTextNode('hospital number:' +data[i]["Number"]));
                divcompenent.appendChild(name);
                divcompenent.appendChild(number);
                li.appendChild(divcompenent);
                list.appendChild(li);
            }

})});