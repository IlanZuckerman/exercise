#!/bin/bash

# this is the wget  bash script
SELF=$0
DURATION=$1
URL=$2

function sighandler(){
    # create child script with same args
    (bash "${SELF} ${DURATION} ${FILE_PATH}")&
}

# define the fork handler in case got signalled with SIGUSR1
trap sighandler SIGUSR1

for t in `seq ${DURATION}`
  do
    wget "${URL}"
    sleep 1
  done