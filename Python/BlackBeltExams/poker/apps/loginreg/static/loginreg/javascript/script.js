
$(document).ready(function(){
$('a').on('click', function(){
    var thisVal = $(this).attr('class');
    var firstVal = $('.button1')
    var secondVal = $('.button2');
    var thirdVal = $('.button3');
    var fourthVal = $('.button4');
    console.log(thisVal);

    if (thisVal == 'button button1 inactive'){
        $(firstVal).removeClass('inactive');
        $(firstVal).addClass('active');
        console.log($(this).attr('class'))
        $(secondVal).addClass('inactive');
        $(secondVal).removeClass('active');
        $(thirdVal).addClass('inactive');
        $(thirdVal).removeClass('active');
        $(fourthVal).addClass('inactive');
        $(fourthVal).removeClass('active');
        console.log("now active");
        console.log('this val' + thisVal)
        console.log('second val:' + secondVal.attr('class'));
        console.log('third val:' + thirdVal.attr('class'));
        console.log('fourth val:' + fourthVal.attr('class'));
    }
    else if (thisVal == 'button button1 active'){
        $(firstVal).removeClass('active');
        $(firstVal).addClass('inactive');
        $(secondVal).addClass('inactive');
        $(secondVal).removeClass('active');
        $(thirdVal).addClass('inactive');
        $(thirdVal).removeClass('active');
        $(fourthVal).addClass('inactive');
        $(fourthVal).removeClass('active');
        console.log("now active");
        console.log('this val' + thisVal)
        console.log('second val:' + secondVal.attr('class'));
        console.log('third val:' + thirdVal.attr('class'));
        console.log('fourth val:' + fourthVal.attr('class'));
    }
    else if (thisVal == 'button button2 inactive'){
        $(secondVal).removeClass('inactive');
        $(secondVal).addClass('active');
        $(thirdVal).addClass('inactive');
        $(thirdVal).removeClass('active');
        $(firstVal).addClass('inactive');
        $(firstVal).removeClass('active');
        $(fourthVal).addClass('inactive');
        $(fourthVal).removeClass('active');
        console.log("now active");
        console.log('this val' + thisVal)
        console.log('second val:' + secondVal.attr('class'));
        console.log('third val:' + thirdVal.attr('class'));
        console.log('fourth val:' + fourthVal.attr('class'));
    }

    else if (thisVal == 'button button2 active'){
        $(secondVal).removeClass('active');
        $(secondVal).addClass('inactive');
        $(firstVal).addClass('inactive');
        $(firstVal).removeClass('active');
        $(thirdVal).addClass('inactive');
        $(thirdVal).removeClass('active');
        $(fourthVal).addClass('inactive');
        $(fourthVal).removeClass('active');
        console.log("now active");
        console.log('this val' + thisVal)
        console.log('second val:' + secondVal.attr('class'));
        console.log('third val:' + thirdVal.attr('class'));
        console.log('fourth val:' + fourthVal.attr('class'));
    }

    else if (thisVal == 'button button3 inactive'){
        $(thirdVal).removeClass('inactive');
        $(thirdVal).addClass('active');
        $(secondVal).addClass('inactive');
        $(secondVal).removeClass('active');
        $(fourthVal).addClass('inactive');
        $(fourthVal).removeClass('active');
        $(firstVal).addClass('inactive');
        $(firstVal).removeClass('active');
        console.log("now active");
        console.log('this val' + thisVal)
        console.log('second val:' + secondVal.attr('class'));
        console.log('third val:' + thirdVal.attr('class'));
        console.log('fourth val:' + fourthVal.attr('class'));
    }

    else if (thisVal == 'button button3 active'){
        $(thirdVal).removeClass('active');
        $(thirdVal).addClass('inactive');
        $(secondVal).addClass('inactive');
        $(secondVal).removeClass('active');
        $(firstVal).addClass('inactive');
        $(firstVal).removeClass('active');
        $(fourthVal).addClass('inactive')
        $(fourthVal).removeClass('active');
        console.log("now active");
        console.log('this val' + thisVal)
        console.log('second val:' + secondVal.attr('class'));
        console.log('third val:' + thirdVal.attr('class'));
        console.log('fourth val:' + fourthVal.attr('class'));
    }

    else if (thisVal == 'button button4 inactive'){
        $(fourthVal).removeClass('inactive');
        $(fourthVal).addClass('active');
        $(secondVal).addClass('inactive');
        $(secondVal).removeClass('active');
        $(thirdVal).addClass('inactive');
        $(thirdVal).removeClass('active');
        $(firstVal).addClass('inactive')
        $(firstVal).removeClass('active');
        console.log("now active");
        console.log('this val' + thisVal)
        console.log('second val:' + secondVal.attr('class'));
        console.log('third val:' + thirdVal.attr('class'));
        console.log('fourth val:' + fourthVal.attr('class'));
    }

    else if (thisVal == 'button button4 active'){
        $(fourthVal).removeClass('active');
        $(fourthVal).addClass('inactive');
        $(secondVal).addClass('inactive');
        $(secondVal).removeClass('active');
        $(thirdVal).addClass('inactive');
        $(thirdVal).removeClass('active');
        $(firstVal).addClass('inactive');
        $(firstVal).removeClass('active');

        console.log("now active");
        console.log('this val' + thisVal)
        console.log('second val:' + secondVal.attr('class'));
        console.log('third val:' + thirdVal.attr('class'));
        console.log('fourth val:' + fourthVal.attr('class'));
    }

    else{
        console.log("now active");
        console.log("thisval:" + thisVal)
        console.log("secondval:" + secondVal.attr('class'))
    }
 
})

});
