#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('An error occurred. Status code:', response.statusCode);
    return;
  }

  const tasks = JSON.parse(body);
  const completed = {};

  for (const task of tasks) {
    if (task.completed) {
      completed[task.userId] = (completed[task.userId] || 0) + 1;
    }
  }

  console.log(completed);
});
