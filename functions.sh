#!/usr/bin/env bash

##
# Print a fatal error and exit
#
function fatalError()
{
    echo "";

    echo -e "[\033[1;31mFATAL ERROR\033[0m]: $1\n";
    exit 1;
}

##
# Print an error message
#
function error()
{
    echo -e "[\033[1;31mERROR\033[0m      ]: $1";
}

##
# Print a success message
#
function success()
{
    echo -e "[\033[1;32mSUCCESS\033[0m    ]: $1";
}

##
# Print a warning message
#
function warning()
{
    echo -e "[\033[1;33mWARNING\033[0m    ]: $1";
}

##
# Print a debug message
#
function debug()
{
    echo -e "\033[1;30m[DEBUG      ]: $1\033[0m" 1>&2;  # Redirige lo stdout su stderr
}

function skip()
{
    echo -e "[\033[1;33mSKIP\033[0m]: $1";
}
