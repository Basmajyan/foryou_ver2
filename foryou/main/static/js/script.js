
window.screen.height;
window.screen.width;
function outZoom() {
    var x = document.getElementById("ZoomImage");
    var y = document.getElementById("Zoom");
    var z = document.getElementById("close");
    var c = document.getElementById("boccheck");
    x.style.opacity = 0;
    x.style.zIndex = -6;
    z.style.zIndex = -5;
    c.style.zIndex = 5;
    z.style.opacity = 0;
    y.style.height = '10px';
}
function Zoom() {
    var x = document.getElementById("ZoomImage");
    var y = document.getElementById("Zoom");
    var z = document.getElementById("close");
    var c = document.getElementById("boccheck");
    x.style.opacity = 1;
    x.style.zIndex = 3;
    z.style.zIndex = 4;
    c.style.zIndex = -4;
    z.style.opacity = 1;
    y.style.height = 'auto';
}

SmoothScroll({
    animationTime: 800,
    stepSize: 75,
    accelerationDelta: 20,
    accelerationMax: 2,
    keyboardSupport: true,
    arrowScroll: 50,
    pulseAlgorithm: true,
    pulseScale: 4,
    pulseNormalize: 1,
    touchpadSupport: true,
})

rbrd.onwheel = function () {
    if (event.ctrlKey) {
        return false;
    }
}

// const nodeArr = new Array(...document.querySelectorAll('.img-wrapper'))
// nodeArr.map(node => node.closest('.user').style.height = node.offsetHeight + 120 + 'px')