function mic() {
    var image = document.getElementById("mic");
    if (image.src.match("image/mic.png")) {
      image.src = "image/mute.png";
    } else {
      image.src = "image/mic.png";
    }
}
  
function hand() {
    var image = document.getElementById("hand");
    if (image.src.match("image/hand.png")) {
      image.src = "image/raise.png";
    } else {
      image.src = "image/hand.png";
    }
}
