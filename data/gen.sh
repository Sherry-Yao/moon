#!/bin/bash

function randpw() {
    local code
    echo "s_id,code"
    for ((i = 0; i < 10000; i++))
    do
        echo -e "0,\c"
        < /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-16};echo;
    done
}

randpw > win_codes.csv
