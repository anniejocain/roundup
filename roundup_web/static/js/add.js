$(document).ready(function() {
    setMaxLength();
    $("#id_description").bind("click mouseover keyup change", function(){checkMaxLength(this.id); } )
});

function setMaxLength() {
  $("#id_description").each(function(i){
    intMax = $(this).attr("maxlength");
    $(this).after("<div><span id='"+this.id+"Counter'>"+intMax+"</span> remaining</div>");
  });
}

function checkMaxLength(strID){ console.log('checking')
  intCount = $("#"+strID).val().length;
  intMax = $("#"+strID).attr("maxlength");
  strID = "#"+strID+"Counter";
  $(strID).text(parseInt(intMax) - parseInt(intCount));
  if (intCount < (intMax * .8)) {$(strID).css("color", "#006600"); } //Good
  if (intCount > (intMax * .8)) { $(strID).css("color", "#FF9933"); } //Warning at 80%
  if (intCount > (intMax)) { $(strID).text(0).css("color", "#990000"); } //Over
}