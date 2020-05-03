var myElement = document.getElementById('detail-container');

// create a simple instance
// by default, it only adds horizontal recognizers
var mc = new Hammer(myElement);
// listen to events...
mc.on("panleft panright tap press", function (ev) {
    if (ev.type === "panleft") {
        window.location.replace(location + "previous");
        mc.stop()
        // djangoRemarkRest.get('http://localhost:8000/polls/2/previous',[])
    } else if (ev.type === "panright") {
        window.location.replace(location + "next");
        mc.stop()
    }
});
