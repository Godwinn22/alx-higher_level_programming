// This is a JavaScript script that fetches the character
// name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (character) {
      $('DIV#character').text(character.name);
    }
  });
});
