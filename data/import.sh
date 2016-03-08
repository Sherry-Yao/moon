#!/bin/bash

mongoimport -d moon -c questions --drop --file ./questions.json --jsonArray
