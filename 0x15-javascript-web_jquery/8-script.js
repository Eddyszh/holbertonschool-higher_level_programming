$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (titles) {
  $.each(titles['results'], function (data, films) {
    $('#list_movies').append('<li>' + films['title'] + '</li>');
  });
}, 'json');
