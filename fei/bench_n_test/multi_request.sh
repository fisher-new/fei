#!/bin/bash
START=$1
END=$2
CACHE_OR_NOCACHE=$3

req() {
    for (( i=${START}; i<${END}; i++ )); do
        curl 127.0.0.1:8000/cache/${CACHE_OR_NOCACHE}/$i/
        echo 
        # curl demo.hhxx.me/cache/cached/${COUNT}/
    done
}

req 
# req &
# req &
# req &
# req &
# req &
# req &
# req &

