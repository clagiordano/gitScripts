#!/usr/bin/env python3
# -*- coding: utf8 -*-

from argparse import ArgumentParser
import os
import sys
from git import Git, Repo


class repoMaintenance(object):
    args = None

    def __init__(self):
        self.__setupArgParser()
        self.__validateArgs()

    def __setupArgParser(self):
        parser = ArgumentParser()
        parser.add_argument("-d", "--directory",
                            help="Source directory", dest="sourceDir", action="store", required=True)

        self.args = parser.parse_args()

    def __validateArgs(self):
        if os.path.isdir(self.args.sourceDir) == False:
            print("Invalid argument path, '%s' isn't a valid directory" %
                  self.args.sourceDir)
            sys.exit(1)

    def __getRepositories(self):
        dirs = {}
        for dir in sorted(os.listdir(self.args.sourceDir)):
            dirPath = os.path.join(self.args.sourceDir, dir)
            if os.path.isdir(dirPath):
                if self.__isRepo(dirPath):
                    dirs[dir] = dirPath

        return dirs

    def __isRepo(self, path):
        try:
            Repo(path)
            return True
        except:
            return False

    def __isRepoByFolder(self, path):
        gitDir = os.path.join(path, '.git')
        if os.path.exists(gitDir):
            if os.path.isdir(gitDir):
                return True

        return False

    def run(self):
        repos = self.__getRepositories()
        print(repos)
        for repo, path in repos.items():
            print("Analyzing repoitory %s ..." % (repo))
            # print("[%10s]: Analyzing repoitory %s..."
            #       % (("SKIPPED", "OK")[self.__isRepo(os.path.join(self.args.sourceDir, repo))], repo))

        # print(repos, len(repos))


if __name__ == '__main__':
    repo = repoMaintenance()

    repo.run()
