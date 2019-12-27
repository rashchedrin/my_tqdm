#!/usr/bin/env bash
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`
python2 ./test_py2.py && echo ${green}OK python2${reset} || echo ${red}FAIL python2${reset}
python3 ./test_py3.py && echo ${green}OK python3${reset} || echo ${red}FAIL python3${reset}
