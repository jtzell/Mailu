#!/usr/bin/python3

import os
import time
import subprocess


command = [
    "certbot",
    "-n", "--agree-tos", # non-interactive
    "-d", os.environ["HOSTNAMES"],
    "-m", "{}@{}".format(os.environ["POSTMASTER"], os.environ["DOMAIN"]),
    "--manual", "--manual-auth-hook", "acme-dns-auth.py",
    "certonly",
    "--cert-name", "mailu",
    "--preferred-challenges", "dns",
    "--keep-until-expiring",
    "--rsa-key-size", "4096",
    "--config-dir", "/certs/letsencrypt",
    "--post-hook", "/config.py",
    "--debug-challenges"
]

# Wait for nginx to start
time.sleep(5)

# Run certbot every hour
while True:
    subprocess.call(command)
    time.sleep(3600)

