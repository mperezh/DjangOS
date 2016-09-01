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
    setTimeout(function () {
        $("#resources").load("reports/resources");
    }, 100);
});

$('#compact').click(function () {
    $("#memory-table").load("/reports/memory-table/compact");
});
