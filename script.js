alert("Hello");

document.getElementById("openButton").onclick = function() {
    var moveButton = document.getElementById("moveButton");
    var currentLeft = parseInt(window.getComputedStyle(moveButton).left, 10);
    moveButton.style.left = (currentLeft + 10000) + 'px';
}

