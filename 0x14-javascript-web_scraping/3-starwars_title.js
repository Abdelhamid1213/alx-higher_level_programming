#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const route = 'https://swapi-api.alx-tools.com/api/films/';

request(route + movieId, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
