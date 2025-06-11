// add a class red when user click on red_header id

$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
