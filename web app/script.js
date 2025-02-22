"use strict";
document.getElementById("add_image").onchange = function (event) {
  var reader = new FileReader();
  reader.onload = function () {
    var preview = document.getElementById("preview");
    preview.src = render.result;
    preview.style.display = "block";
  };

  reader.readAsDataURL(event.target.files[0]);
};
