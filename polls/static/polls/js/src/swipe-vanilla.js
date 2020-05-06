var element = document.getElementById('mySwipe');
window.mySwipe = new Swipe(element, {
    startSlide: 1,
    // auto: 3000,
    draggable: true,
    autoRestart: false,
    continuous: true,
    disableScroll: true,
    stopPropagation: true,
    callback: function (index, element) {
    },
    transitionEnd: function (index, element) {
        if (index === 0) {
            window.location.replace(location + "previous");
        } else if (index === 2) {
            window.location.replace(location + "next");
        }
    }
});
