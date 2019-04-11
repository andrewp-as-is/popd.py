#!/usr/bin/env python
import os
import popd


@popd.popd
def test():
    os.chdir("/tmp")


cwd = os.getcwd()
test()
assert cwd == os.getcwd()
