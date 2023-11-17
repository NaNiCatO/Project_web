function like() {
  var image = document.getElementById("like");
  if ( image.innerHTML == "👍🏿" ) {
    image.innerHTML = "👍";
  } else {
    image.innerHTML = "👍🏿";
  }
}