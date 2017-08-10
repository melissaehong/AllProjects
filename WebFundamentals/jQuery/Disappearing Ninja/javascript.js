var htmlString = '';

for (var i = 0; i < 8; i++){
  htmlString += '<img src = "amsterdam.jpg" alt="amsterdam picture">';
}

htmlString += '<button>restore</button>';

$(document).ready(function(){
  $('#container').append(htmlString);

  $('img').click(function(){
    $(this).hide('fast');
  });

  $('button').click(function(){
    $('img').show();
  });
});
