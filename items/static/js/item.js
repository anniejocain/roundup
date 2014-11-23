$(document).ready(function(){

    // Get our org's links from the API and print them here on load
    var request = $.ajax({
        url: settings.url,
        type: "GET",
        dataType: "json"
    });
    
    request.done(function(data) {
    	var source = $("#item-template").html();
    	var template = Handlebars.compile(source);
        $('#item-container').html(template({'item': data}));
    	

    });
    request.fail(function(jqXHR) {
        // We should print some helpful fail message
    });

});
