const body_w = document.getElementById("body_w");

function toggle_weather(state_w) {
    if (state_w) {
        console.log("false");
        body_w.style.background = "linear-gradient(to bottom, #001b92 0%, #1a1a1a 100%)";
        body_w.style.height = "947px";
    } else {
        console.log("true");
        body_w.style.background = "linear-gradient(to bottom, #ffae00 0%, #ff0101 100%)";
        body_w.style.height = "947px";
    }
}