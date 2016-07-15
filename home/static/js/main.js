function resizeDiv() {
    var vph = $(window).height() - $('.mdl-mini-footer').outerHeight();
    var vphp = vph - $('#status-bar').outerHeight();
    $('#desktop-background').css({'height': vph + 'px'});
    $('#desktop').css({'height': vph + 'px'});
    $('#program').css({'height': vphp + 'px'});
}

$(document).ready(function () {
    resizeDiv();
});

window.onresize = function (event) {
    resizeDiv();
}

$('.chrome-app').click(function () {
    $("#desktop").load("apps/chrome #program-window");
});

