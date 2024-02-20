#!/usr/bin/node

const request = require('request');
const route = process.argv[2];
let c = 0;

request(route, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    for (const film of data.results) {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        c++;
      }
    }
    console.log(c);
  }
});
