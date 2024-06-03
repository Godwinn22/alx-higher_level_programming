// This is a JavaScript script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$(document).ready(function () {
	const apiurl = 'https://swapi-api.alx-tools.com/api/films/?format=json'
	$.ajax({
		url: apiurl,
		method: 'GET',
		success: function (movie_data) {
			const movies = movie_data.results
			$.each(movies, function (i, movie) {
				const title = movie.title
				$('#list_movies').append(`<li>${title}</li>`)
			})
		}
	})
})