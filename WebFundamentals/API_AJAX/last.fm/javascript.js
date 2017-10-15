$(function (){
    var $orders = $('#orders');
    var $drink = $('#drink');
    var $name = $('#name')

    $.ajax({
        type: 'GET',
        url: 'http://www.last.fm/api/auth/?api_key=9bdb5b26ea143efbdaafb28956a2f405',
        success: function(orders){
            $.each(orders, function(i, order){
                $orders.append('<li>name: ' + order.name + ', drink: '+ order.drink + '</li>');
            })
        }
    })
    $('#add-order').on('click', function(){

        var order = {
            name: $name.val(),
            drink: $drink.val(),
        }
        $.ajax({
            type: 'POST',
            url: 'http://rest.learncode.academy/api/melissa/orders',
            data: order,
            success: function(newOrder){
                $orders.append('<li>name: '+ newOrder.name +', drink: '+ newOrder.drink + '</li>');
            }
            })
        })
    })