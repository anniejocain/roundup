var item_url = web_base + "api/item";
$(document).ready(function() {
 
  showHopper();
 
});

function showHopper() {
  $.getJSON(item_url + '/recent?callback=?', function(data) {
    var items = [];
    $.each(data, function(key, val) {
      items.push('<p><a href="' + val.link + '">' + val.title + '</a><br>' + val.description + '<br><small>- ' + val.creator + '</small>');
    });
    var ul = items.join('');
    
    $('#hopper').html(ul);
});
}

