$(document).ready(function(){
    $("span").click(function(){
      $(this).siblings().slideToggle();
     });
  }); 

$(document).ready(function(){
  $("#postForm").click(function(){
    $.ajax({
      type: 'POST'
    })
    location.reload();
    });
}); 