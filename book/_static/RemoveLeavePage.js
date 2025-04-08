//Polling to set onbeforeunload to null when it is overwritten by thebe,
//so that users are not prompted to confirm leaving the page
var polling_unload = setInterval(() => {
    if (window.onbeforeunload !== null) {
        window.onbeforeunload = null;
        clearInterval(polling_unload);
    }
}, 100);