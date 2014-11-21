var gallery_id;

$(document).ready(function() {
    setMaxLength();
    $("#id_description").bind("click mouseover keyup change", function(){checkMaxLength(this.id); } )
    
    // Check our status service to see if we have archiving jobs pending
	var request = $.ajax({
	    type: "POST",
		url: 'http://localhost:8000/service/gallery/',
		data: { target_url: $("#id_link").val()},
		cache: false
	});

    request.done(function( msg ) {
      gallery_id = msg.gallery_id;
      setInterval(check_status, 1000);
    });

    request.fail(function( jqXHR, textStatus ) {
      alert( "Request failed: " + textStatus );
    });
    
});

function setMaxLength() {
  $("#id_description").each(function(i){
    intMax = $(this).attr("maxlength");
    $(this).after("<div><span id='"+this.id+"Counter'>"+intMax+"</span> remaining</div>");
  });
}

function checkMaxLength(strID){
  intCount = $("#"+strID).val().length;
  intMax = $("#"+strID).attr("maxlength");
  strID = "#"+strID+"Counter";
  $(strID).text(parseInt(intMax) - parseInt(intCount));
  if (intCount < (intMax * .8)) {$(strID).css("color", "#006600"); } //Good
  if (intCount > (intMax * .8)) { $(strID).css("color", "#FF9933"); } //Warning at 80%
  if (intCount > (intMax)) { $(strID).text(0).css("color", "#990000"); } //Over
}

function check_status() {


    // Check our status service to see if we have any new images in our gallery
	var request = $.ajax({
		url: 'http://localhost:8000/service/gallery/?gallery_id=' + gallery_id,
		type: "GET",
		dataType: "json",
		cache: false
	});

	request.done(function(data) {
	    var source = $("#image-template").html();
    	var template = Handlebars.compile(source);
        $('#gallery_container').html(template({'item': data}));
	});
}

/* Our polling function for the thumbnail completion - end */