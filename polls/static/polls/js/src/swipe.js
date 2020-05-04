var myElement = document.getElementById('detail-container');

// create a simple instance
// by default, it only adds horizontal recognizers
var mc = new Hammer(myElement);
// listen to events...
mc.on("panleft panright tap press", function (ev) {
    if (ev.type === "panleft" && ev.deltaX < -100 && Math.abs(ev.deltaY) < 25) {
        window.location.replace(location + "next");
        mc.stop()
    } else if (ev.type === "panright" && ev.deltaX > 100 && Math.abs(ev.deltaY) < 25) {
        window.location.replace(location + "previous");
        mc.stop()
    }
});
