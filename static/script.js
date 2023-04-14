$(document).ready(function(){
    $(".targFlip").click(function(){
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