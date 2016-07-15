$(document).ready(function () { resizeDiv(); });

window.onresize = function (event) { resizeDiv(); }

function resizeDiv() {
    //var vph = $(window).height();
    //var vphp = $(window).height();
    var vph = $(window).height() - $('.mdl-mini-footer').outerHeight();
    var vphp = $(window).height() - $('.mdl-mini-footer').outerHeight() - $('#status-bar').outerHeight();
    $('#desktop-background').css({'height':vph + 'px'});
    $('#desktop').css({'height':vph + 'px'});
    $('#program').css({'height':vphp + 'px'});
    //$('#program').css({'height':vph + 'px'});
}