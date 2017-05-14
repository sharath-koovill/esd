$(document).ready(function(){

$("#search_button").click(function(){
   var name = $("#id_name").val();
   var profession = $("#id_profession").val();
   var location = $("#id_location").val();
   var currentUrl = window.location.href;
   var baseUrl = currentUrl.split("?")[0];
   var final = baseUrl + "?name=" + name + "&profession=" + profession + "&location=" + location;
   window.open(final,"_self");
   //location.replace(final);
   //alert(final);
});
   
});

