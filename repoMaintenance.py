#!/usr/bin/env python3
# -*- coding: utf8 -*-

from argparse import ArgumentParser
import os
import sys
from git import Git, Repo
from subprocess import Popen, run

class repoMaintenance(object):
    args = None
    stats = {
        'repoCount': 0,
        'totalSize': 0,
        'freedSpace': 0
    }

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

    def __doMaintenance(self, path):
        os.chdir(path)

        Popen(["git", "fetch"])
        Popen(["git", "pull", "origin"])

        proc = run(["du", "-s"], capture_output=True)
        # repoSize = int(os.popen("du -s").read().strip())
        # repoSize, err = proc.communicate()

        # print(str(proc.stdout))
        # sys.exit(1)

        self.stats['repoCount'] += 1
        # self.stats['totalSize'] += repoSize
        # print(cmd)

    def run(self):
        repos = self.__getRepositories()
        # print(repos)
        for repo, path in repos.items():
            print("Analyzing repoitory %s ..." % (repo))
            self.__doMaintenance(path)
        # print(repos, len(repos))

        print(self.stats)


if __name__ == '__main__':
    repo = repoMaintenance()

    repo.run()
