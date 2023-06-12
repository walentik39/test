#!/usr/bin/env python3

import subprocess

ip_list = ['8.8.4.4','127.0.1.1','test.me','37.214.18.10','8.8.8.8']
for ip in ip_list:
    result = subprocess.run(
            ['ping','-c','1','-n', ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8"
            )
    output = result.stderr + result.stdout
    print(output)
    if result.returncode == 0:
        print(f"Адрес {ip} пингуется")
    else:
        print(f"адрес {ip} не пингуется")
