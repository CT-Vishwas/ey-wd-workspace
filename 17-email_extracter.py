#!/usr/bin/env python
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
import re
def read_file(fname):
    try:
        with open(fname) as fh:
            return fh.read()
    except FileNotFoundError:
        print("File you are trying to read does not exist")

def email_extracter(inp_text):
    pat = r"[a-z0-9.]+@[a-z.]+"
    return re.findall(pat, inp_text)

if __name__ == '__main__':
    fname = "random_emails_text.txt"
    content = ""
    with open(fname) as fh:
        content = fh.read()
    
    extracted_emails = email_extracter(content)
    print(f"{len(extracted_emails)}")
# Starts with a letter
# can contain . 
# .com/.edu/.net/.co/.io -ending with this