// Get the modal
var tmodal = document.getElementById("newtypeModal");

// opens the modal
var tbtn = document.getElementById("newtypeBtn");

// Get the <span> element that closes the modal
var tspan = document.getElementsByClassName("close")[0];

// clicks , open the modal
tbtn.onclick = function() {
  tmodal.style.display = "block";
}

// <span> (x), close the modal
tspan.onclick = function() {
  tmodal.style.display = "none";
}

var rmodal = document.getElementById("newrepairModal");
var rbtn = document.getElementById("newrepairBtn");
var rspan = document.getElementsByClassName("close")[1];

rbtn.onclick = function() {
  rmodal.style.display = "block";
}
rspan.onclick = function() {
  rmodal.style.display = "none";
}
