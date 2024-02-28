$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    dataType: 'json',
    success: function (data) {
      for (const film of data.results) {
        $('UL#list_movies').append(`<li>${film.title}</li>`);
      }
    },
    error: function () {
      $('UL#list_movies').html('Error fetching data');
    }
  });
});
