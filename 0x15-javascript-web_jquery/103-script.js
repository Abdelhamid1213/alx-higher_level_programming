$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    fetchTranslation();
  });

  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const code = $('INPUT#language_code').val();

    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + code,
      success: function (data) {
        $('DIV#hello').html(data.hello);
      },
      error: function () {
        $('DIV#hello').text('Error fetching translation');
      }
    });
  }
});
