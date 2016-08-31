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
    $("#memory-table").load("reports/memory-table/show");
    setTimeout(function() {
        $("#resources").load("reports/resources");
    }, 100);
});

$('.chrome-app').click(function () {

    $("#memory-table").load("reports/memory-table/add/chrome");
    setTimeout(function() {
        $("#processes-table").load("reports/processes/add/chrome");
    }, 100);

    setTimeout(function() {
        $("#resources").load("reports/resources");
    }, 100);

    $("#desktop").load("apps/open/chrome");
    resizeDiv();
});

$('.folders-app').click(function () {

    $("#memory-table").load("reports/memory-table/add/folders");
    setTimeout(function() {
        $("#processes-table").load("reports/processes/add/folders");
    }, 100);

    setTimeout(function() {
        $("#resources").load("reports/resources");
    }, 100);

    $("#desktop").load("apps/open/folders");
    resizeDiv();
});

$('.calculator-app').click(function () {

    $("#memory-table").load("reports/memory-table/add/calculator");
    setTimeout(function() {
        $("#processes-table").load("reports/processes/add/calculator");
    }, 100);

    setTimeout(function() {
        $("#resources").load("reports/resources");
    }, 100);

    $("#desktop").load("apps/open/calculator");
    resizeDiv();
});

$('#compact').click(function () {
    setTimeout(function() {
        $("#memory-table").load("/reports/memory-table/compact");
    }, 100);
});
