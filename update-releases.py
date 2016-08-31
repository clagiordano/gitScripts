#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2016 Claudio Giordano <claudio.giordano@autistici.org>
#
#  Homepage https://github.com/clagiordano/gitScripts.git
#  Homepage https://clagiordano@bitbucket.org/clagiordano/gitscripts.git
#  License GPLv3 https://www.gnu.org/licenses/gpl.html

import argparse
import os
from subprocess import call

"""
Local import
"""
import modules.outputUtils as out

class updateReleases(object):
    """
    """
    def setArgParser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-r", "--release", action='store', required=True,
                            help="Release, tag or commit id to update")
        parser.add_argument("-d", "--directories", action='store', required=True,
                            help="Comma separated directories to update")
        parser.add_argument("-e", "--execute", action='store', required=True,
                            help="Commands string to execute into repository")

        self.args_parsed = parser.parse_args()

    def analyzeFolders(self):
        self.directories = self.args_parsed.directories.split(',')
        if len(self.directories) <= 0:
            out.fatalError("Invalid directories list")

    """
    """
    def __init__(self):
        self.setArgParser()
        self.working_dir = os.getcwd()
        self.analyzeFolders()

if __name__ == "__main__":
    call("clear")
    ur = updateReleases()


#
# if [ $# -eq 0 ]
# then
#     usage;
# else
#     ARGDIRS=$*;
# fi
#
# echo "ARGDIRS: '${ARGDIRS}'";
#
# success "Start repository update...";
#
# for REPOSITORY in ${ARGDIRS}
# do
#     DIRECTORY=${BASEDIR}${REPOSITORY};
#     if [ -d ${DIRECTORY} ]
#     then
#         success "Check repository ${DIRECTORY}... ";
#         if eval "cd ${DIRECTORY}"
#         then
#             if [ -d ".git" ]
#             then
#                 success "Executing commands into repository... ";
#
#                 OLD_BRANCH=$(git branch | grep '\*' | sed 's/^.\ //');
#                 debug "OLD_BRANCH: ${OLD_BRANCH}";
#
#                 if eval "git fetch --all -q"
#                 then
#                     success "Fetch all remotes";
#                 else
#                     error "Fetch all remotes";
#                 fi
#             fi
#         fi
#     else
#         warning "Skipping invalid repository '${DIRECTORY}'";
#     fi
# done
#
# exit 0
