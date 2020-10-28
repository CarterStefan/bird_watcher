$(document).ready(function(){
    $(".sidenav").sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.datepicker').datepicker({
        format: "dd/mm/yyyy"
    });  
  });

// Fix for 'required' on sleect forms found on stack overflow 
$("select[required]").css({display: "block", height: 0, padding: 0, width: 0, position: 'absolute'});