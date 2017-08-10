var htmlS = '';

for (var i = 0; i < 8; i++){
  htmlS += '<img src = "amsterdam.jpg" alt = "amsterdam picture">';
}

htmlS += '<button> restore me! </button>';

$(document).ready(function(){
  $('#container').append(htmlS);

  $('img').click(function(){
    $(this).hide('slow');
  });

  $('button').click(function(){
    $('img').show();
  });
});
