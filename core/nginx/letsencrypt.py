#!/usr/bin/python3

import os
import time
import subprocess


command = [
    "certbot",
    "-n", "--agree-tos", # non-interactive
    "-d", os.environ["HOSTNAMES"],
    "-m", "{}@{}".format(os.environ["POSTMASTER"], os.environ["DOMAIN"]),
    "--authenticator", "certbot-dns-acmedns:dns-acmedns",
    "--certbot-dns-acmedns:dns-acmedns-credentials", "/conf/acmedns-credentials.ini",
    "certonly",
    "--cert-name", "mailu",
    "--preferred-challenges", "dns",
    "--keep-until-expiring",
    "--rsa-key-size", "4096",
    "--config-dir", "/certs/letsencrypt"
]

# Wait for nginx to start
time.sleep(5)

# Run certbot every hour
while True:
    subprocess.call(command)
    subprocess.call([
        "python3",
        "/config.py"
    ])
    time.sleep(3600)

