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
    $("#swap-table").load("reports/swap-table/show");
    $("#disk-vector").load("reports/resources/disk");
    setTimeout(function () {
        $("#resources").load("reports/resources");
    }, 100);
});

$('#fixed-tab-1').click(function () {
    $("#resources").load("reports/resources");
});

$('#compact').click(function () {
    $("#memory-table").load("/reports/memory-table/compact");
});

$('#fifo-btn').click(function () {
    $("#fifo").load("/reports/resources/disk/fifo");
});

$('#scan-btn').click(function () {
    $("#scan").load("/reports/resources/disk/scan");
});

$('#cscan-btn').click(function () {
    $("#csan").load("/reports/resources/disk/cscan");
});