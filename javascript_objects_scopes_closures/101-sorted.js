#!/usr/bin/node

const { dict } = require('./101-data');

const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  const strValue = value.toString();
  if (!(strValue in newDict)) {
    newDict[strValue] = [];
  }
  newDict[strValue].push(key.toString());
}
