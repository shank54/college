$(document).ready(function(){
    $("input").keyup(function(){
    if (this.value.length > 0){
        $('#list').show();
        }
    else{
        $('#list').hide();
    }
    });
});
   $("#container-fluid").click(function(){
    $("#list").hide();
});