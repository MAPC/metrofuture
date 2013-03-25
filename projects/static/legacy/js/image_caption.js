/*$Id: image_caption.js,v 1.1 2008/02/23 06:24:07 davidwhthomas Exp $*/
$(document).ready(function(){
  $("img.caption").each(function(i) {
    var imgwidth = $(this).width();
    var imgheight = $(this).height();
    var iwidth = $(this).attr('width');
    var captiontext = $(this).attr('alt');
    var alignment = $(this).attr('align');
    $(this).attr({align:""});
    $(this).wrap("<div class=\"image-caption-container\" style=\"float:" + alignment + "; width:" + iwidth + "px; display:inline;\"></div>");
    $(this).parent().width(imgwidth);
    $(this).parent().append("<div class=\"image-caption\">" + captiontext + "</div>");
  });
});
