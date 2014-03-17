#!/usr/bin/env python

##############################################################################
# Copyright 2014 Joseph Chilcote
# 
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not
#  use this file except in compliance with the License. You may obtain a copy
#  of the License at  
# 
#       http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
##############################################################################

import subprocess, sys, json

def facter(key):
        p = subprocess.Popen(['facter', '--json'], stdout=subprocess.PIPE)
        p.wait()
        lines = p.stdout.readlines()
        data = json.loads(lines[0])
        if key == 'all':
                for k, v in sorted(data.items()):
                        print "%s: %s" % (k, v)
        else:
                return data[key]

def main():
        if len(sys.argv) == 1:
                facter('all')
        elif len(sys.argv) == 2:
                print facter(sys.argv[1])
        else:
                print "Usage: ./pyfacter.py <key>"

if __name__ == "__main__":
        main()
