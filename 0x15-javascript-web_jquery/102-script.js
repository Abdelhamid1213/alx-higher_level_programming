$(document).ready(function () {
  $('INPUT#btn_translate').on('click', () => {
    const code = $('INPUT#language_code').val();

    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + code,
      success: (data) => {
        $('DIV#hello').html(data.hello);
      },
      error: () => {
        $('DIV#hello').text('Error fetching translation');
      }
    });
  });
});
