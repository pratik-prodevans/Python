#!/usr/bin/python

import os
import crypt

password="demo123"
enpass= crypt.crypt(password, "22")
os.system("useradd -p "+enpass+" demo123")

