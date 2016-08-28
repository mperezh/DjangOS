function resizeDiv() {
    var vph = $(window).height() - $('.mdl-mini-footer').outerHeight();
    var vphp = vph - $('#status-bar').outerHeight();
    $('#desktop-background').css({'height': vph + 'px'});
    $('#desktop').css({'height': vph + 'px'});
    $('#program').css({'height': vphp + 'px'});
}

window.onresize = function (event) {
    resizeDiv();
};

$(document).ready(function () {
    resizeDiv();
    $("#processes-table").load("reports/processes/add/system");
    //$("#resources").load("reports/resources");
    setTimeout(function() {
        $("#resources").load("reports/resources");
    }, 100);
});

$('.chrome-app').click(function () {
    $("#desktop").load("apps/open/chrome");
    $("#processes-table").load("reports/processes/add/chrome");
    setTimeout(function() {
        $("#resources").load("reports/resources");
    }, 100);
    resizeDiv();
});

$('.calculator-app').click(function () {
    $("#desktop").load("apps/open/calculator");
    $("#processes-table").load("reports/processes/add/calculator");
    setTimeout(function() {
        $("#resources").load("reports/resources");
    }, 100);
    resizeDiv();
});

$('.folders-app').click(function () {
    $("#desktop").load("apps/open/folders");
    $("#processes-table").load("reports/processes/add/folders");
    setTimeout(function() {
        $("#resources").load("reports/resources");
    }, 100);
    resizeDiv();
});