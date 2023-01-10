$(document).ready(function () {
  $("#datedropper").dateDropper({});
  var $submit = $("#submit_prog").hide();
  var $bank = $("#accountForm").hide();
  var $email = $("#emailForm").hide();
  $cbs = $('input[name="id_meja"]').click(function () {
    $submit.toggle($cbs.is(":checked"));
    $bank.toggle($cbs.is(":checked"));
    $email.toggle($cbs.is(":checked"));
  });
  $(".checkoption").click(function () {
    $(".checkoption").not(this).prop("checked", false);
  });
});

// function checkedOnClick(el) {
//   // Select all checkboxes by class
//   var checkboxesList = document.getElementsByClassName("checkoption");
//   for (var i = 0; i <= checkboxesList.length; i++) {
//     checkboxesList.item(i).checked = false; // Uncheck all checkboxes
//   }

//   el.checked = true; // Checked clicked checkbox
// }

// $('input[name="id_meja"]').change(function () {
//   var submitBtn = $("#submit_prog").hide();
//   var bank = $("#account").hide();
//   var email = $("#email").hide();
//   if ($('input[name="id_meja"]:checked').length > 0) {
//     email.toggle();
//     bank.toggle();
//     submitBtn.toggle();
//   }
// });
var svg = d3.select("svg");
var originX = 200;
var originY = 200;
var innerCircleRadius = 40;
var outerCircleRadius = 60;

var table = svg.append("circle").attr({
  cx: originX,
  cy: originY,
  r: innerCircleRadius,
  fill: "white",
  stroke: "black",
});

var outerCircle = svg.append("circle").attr({
  cx: originX,
  cy: originY,
  r: outerCircleRadius,
  fill: "none",
  stroke: "black",
});

var chairOriginX = originX + outerCircleRadius * Math.sin(0);
var chairOriginY = originY + outerCircleRadius * Math.cos(0);

var chairWidth = 20;
var chair = svg.append("rect").attr({
  x: chairOriginX - chairWidth / 2,
  y: chairOriginY - chairWidth / 2,
  width: chairWidth,
  opacity: 1,
  height: 20,
  fill: "none",
  stroke: "blue",
});

chair.attr("transform", "rotate(45, 200, 200)");
