#!/bin/bash

mongoimport -d moon -c questions --drop --file ./questions.json --jsonArray
mongoimport -d moon -c codes --drop --type csv --file ./win_codes.csv --headerline
