$(document).ready(function(){
  $('form').submit(function(){
    $.post($(this).attr('action'), $(this).serialize(), function(notes){
      console.log(notes);
      $('#notes').html(notes);
      $('input[type="text"]').val('');
    }, 'html');
    return false;
  });

  $('#notes').on('submit', 'form', function(){
    $.get($(this).attr('action'), function(notes){
      $('#notes').html(notes);
    }, 'html');
    return false;
  });

  $('#notes').on('focusout', 'textarea', function(){
    console.log(this);
    console.log($(this).parent());

    $.post($(this).parent().attr('action'), $(this).serialize($(this).val()), function(notes){
      $('#notes').html(notes);
    }, 'html');
    });

  })
  })
});
