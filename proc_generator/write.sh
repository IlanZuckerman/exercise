#!/bin/bash

# this is the file writer bash script
SELF=$0
DURATION=$1
FILE_PATH=$2
#LOCK_DIR="/tmp/lock"

function sighandler
{
#     create child script with same args
    bash ${SELF} ${DURATION} ${FILE_PATH} &
}

# define the fork handler in case got signalled with SIGUSR1
trap sighandler SIGUSR1

for t in `seq ${DURATION}`
  do
#    mkdir ${LOCK_DIR} && (echo "This is my time to shine" >> ${FILE_PATH} ; rmdir ${LOCK_DIR})
    echo "This is my time to shine" >> ${FILE_PATH}
    sleep 1
  done