/*function date() {

    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1; //January is 0!
    var yyyy = today.getFullYear();

    if (dd < 10) {
        dd = '0' + dd
    }

    if (mm < 10) {
        mm = '0' + mm
    }

    today = mm + '/' + dd + '/' + yyyy;
    document.getElementById("date").innerHTML = today.toString();
}*/

function checkTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    //var s = today.getSeconds();
    // add a zero in front of numbers<10
    m = checkTime(m);
    //s = checkTime(s);
    document.getElementById('time').innerHTML = h + ":" + m;
    t = setTimeout(function () {
        startTime()
    }, 500);
}

startTime();
//date();