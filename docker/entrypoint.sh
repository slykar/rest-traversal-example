#!/bin/bash

if ! $INI_FILE; then
    echo "No INI file was specified. use -e INI_FILE=<your_file>"
fi

if [ "$1" = 'pserve' ]; then
    pserve --reload $INI_FILE
fi
