#!/usr/bin/env python3
# -*- coding: utf8 -*-

from argparse import ArgumentParser
import os, sys
from git import Repo

class repoMaintenance(object):
    args = None

    def __init__(self):
        self.__setupArgParser()
        self.__validateArgs()

        print("sourceDir: %s" % self.args.sourceDir)

    def __setupArgParser(self):
        parser = ArgumentParser()
        parser.add_argument("-d", "--directory",
            help="Source directory", dest="sourceDir", action="store", required=True)

        self.args = parser.parse_args()

    def __validateArgs(self):
        if os.path.isdir(self.args.sourceDir) == False:
            print("Invalid argument path, '%s' isn't a valid directory" % self.args.sourceDir)
            sys.exit(1)

    def __getRepositories(self):
        return os.listdir(self.args.sourceDir)

    def __isRepo(self, path):
        try:
            repo = Repo(path)
            repo.head
            return True
        except:
            return False
        # print(repo.head)

    def run(self):
        repos = self.__getRepositories()
        for repo in repos:
            print("Analyzing repoitory %s... %s" % (repo, ("OK", "SKIPPED")[self.__isRepo(repo)]))

        # print(repos, len(repos))

if __name__ == '__main__':
    repo = repoMaintenance()

    repo.run()
