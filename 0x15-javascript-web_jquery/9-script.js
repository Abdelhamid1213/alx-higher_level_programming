$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    },
    error: function () {
      $('DIV#hello').text('Error fetching translation');
    }
  });
});
