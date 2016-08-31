#!/usr/bin/env bash

#  Copyright 2016 Claudio Giordano <claudio.giordano@autistici.org>
#
#  Homepage https://github.com/clagiordano/gitScripts.git
#  Homepage https://clagiordano@bitbucket.org/clagiordano/gitscripts.git
#  License GPLv3 https://www.gnu.org/licenses/gpl.html

clear;

IFS='
';

CURDIR=$(pwd);
BASEDIR="";

. functions.sh

function usage() {
    echo "Usage: $0 [branch|tag|commit] [repositories]";
    exit 1;
}

if [ $# -eq 0 ]
then
    usage;
else
    ARGDIRS=$*;
fi

echo "ARGDIRS: '${ARGDIRS}'";

success "Start repository update...";

for REPOSITORY in ${ARGDIRS}
do
    DIRECTORY=${BASEDIR}${REPOSITORY};
    if [ -d ${DIRECTORY} ]
    then
        success "Check repository ${DIRECTORY}... ";
        if eval "cd ${DIRECTORY}"
        then
            if [ -d ".git" ]
            then
                success "Executing commands into repository... ";

                OLD_BRANCH=$(git branch | grep '\*' | sed 's/^.\ //');
                debug "OLD_BRANCH: ${OLD_BRANCH}";

                if eval "git fetch --all -q"
                then
                    success "Fetch all remotes";
                else
                    error "Fetch all remotes";
                fi
            fi
        fi
    else
        warning "Skipping invalid repository '${DIRECTORY}'";
    fi
done

exit 0
