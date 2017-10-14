// Once more, formatting this in a slight more clear format (if longer vertically)
$(document).ready(
    function( ) {
        $('form').submit(
            function( ) {
                // load up any gif you want, this will be shown while user is waiting for response
                $.post(
                    $(this).attr('action'),
                    $(this).serialize( ),
                    function(res) {
                        // pay careful attention to the response object
                        console.log('the response object:');
                        console.log(res);
                        var html_string = "";
                        if (res.results.length !== 0) {
                            html_string = "<video controls src='" + res.results[0].previewUrl + "'></video>";
                        }
                        else {
                            html_string = "Not Found";
                        }
                        console.log('the html string:');
                        console.log(html_string);
                    },
                    'json'
                );
                // don't forget this 'false' -- without it, the 'submit' cycle will continue, and the page will refresh
                return false;
            }
        );
    }
);