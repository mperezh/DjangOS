/*$(document).ready(function () {
    var desktop = $('#desktop');
    $(window).height();
});*/

$(document).ready(function () { resizeDiv(); });

window.onresize = function (event) { resizeDiv(); }

function resizeDiv() {
    //vpw = $(window).width();
    var vph = $(window).height();
    vph = vph - $('.mdl-mini-footer').outerHeight()
    $('#desktop').css({'height':vph + 'px'});
    $('#desktop-background').css({'height':vph + 'px'});
}