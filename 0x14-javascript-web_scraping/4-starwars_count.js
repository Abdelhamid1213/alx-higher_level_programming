#!/usr/bin/node

const request = require('request');
const route = process.argv[2];
let c = 0;

request(route, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
