#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(path, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
