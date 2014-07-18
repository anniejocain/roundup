var item_url = web_base + "api/item";
var blog_url = web_base + "api/blog";
var tipped = false;
$(document).ready(function() {
  setMaxLength();
  $("textarea.checkMax").bind("click mouseover keyup change", function(){checkMaxLength(this.id); } )
  showHopper();
  $("#share-form").validate({
    submitHandler: function(form) {
      var title = $('#title').val();
      var url = $('#url').val();
      var creator = $('#creator').val();
      var description = $('#description').val();
      var intro = '';
      if(tipped)
        intro = $('#intro').val();
      $.post(item_url, {title: title, creator: creator, link: url, description: description, intro: intro}, function(data) {
        $('#share-form').slideUp();
        $('#share-form input, #share-form textarea').each(function() {
              $(this).val('');
        });
        $('#result').html('<h4>' + data.response + '</h4>');
        if(data.tipped) {
            $('#blog-post').fadeIn();
        }
        showHopper();
      });
      return false;	
    }
   });
   
   $("#blog-post").submit(function(event) {
     var intro = $('#intro').val();
     $.post(blog_url, {intro: intro}, function(data) {
        $('#blog-post').fadeOut();
        $('#result').html('<h4>' + data.response + '</h4>');
      });
      return false;	
    });
	
	$('#bookmarklet-name').keyup(function() {
	  var name = $(this).val();
	  var bookmarklet = "javascript:(function(){%20window.open(%22" + web_base + "add?link=%22+encodeURIComponent(%20location.href)+%22&title=%22+encodeURIComponent(document.title)+%22&name=" + name + "%22);%20})();"
	  $("#bookmarklet").attr('href', bookmarklet);
	});
	
	$('#get').collapse("hide");
	
	$("#intro").focus(function() {
        var $this = $(this);
        $this.select();
        // Work around Chrome's little problem
        $this.mouseup(function() {
            // Prevent further mouseup intervention
            $this.unbind("mouseup");
            return false;
        });
    });
});

function showHopper() {
  $.getJSON(item_url + '/recent?callback=?', function(data) {
    var items = [];
    if(data.tipped) {
        $('#roundup-only').hide();
        $('#blog-post').show();
        tipped = true;
    }
    
    $.each(data.items, function(key, val) {
      items.push('<p><a href="' + val.link + '">' + val.title + '</a><br>' + val.description + '<br><small>- ' + val.creator + '</small>');
    });
    var ul = items.join('');
    
    $('#hopper').html(ul);
});
}

function setMaxLength() {
  $("textarea.checkMax").each(function(i){
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
