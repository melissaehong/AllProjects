$(document).ready(function(){
  $('#formcreate').submit(function(){
    $.post('/notes/create', $(this).serialize(), function(data){
      $('#notes').html(data);
    });
    return false;
  });
  $('#notes').on('submit', 'form', function(){
    $.get($(this).attr('action'), function(notes){
      $('#notes').html(notes);
    } 'html' };
    })
    })
  })
});
