// This is a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello.

$(document).ready(function () {
  const apiurl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.ajax({
    type: 'GET',
    url: apiurl,
    success: function (hello) {
      $('DIV#hello').text(hello.hello);
    },
    error: function (error) {
      console.error('Error fetching data', error);
    }
  });
});
