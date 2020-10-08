$(document).ready(function(){
    $(".sidenav").sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.datepicker').datepicker({
        format: "dd/mm/yyyy"
    });
  });