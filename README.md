# zkteco-bruteforce

ZKTeco generally uses port 4370 for communication purpose without any password.

For hardening it, people generally put a communication password so that others can not connect to it. However, there's a issue that this password is only numeric with 4 characters only.
So I've written a simple script for brute-forcing purpose to find the configured password at port 4370.

This script is for Educational Purpose only and I bear no responsibility if someone uses it for malicious purpose.

# Requirements
pip install -U pyzk
