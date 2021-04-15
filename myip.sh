#!/bin/bash
echo "This tools used to display ip address!"

echo "hostname: $(hostname)"

echo "ipv4 address: $(hostname -I | cut -d " " -f 1)"

echo "ipv6 address: $(hostname -I | cut -d " " -f 2)"
