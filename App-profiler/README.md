# AIP

## Usage
`  python .\test-app.py 100 `

## VCL installation


https://www.tecmint.com/commands-to-collect-system-and-hardware-information-in-linux/

## commands to check infra config of devices
uname -a 
sudo lshw
lscpu
lsblk -a
lsusb
lspci 
sudo fdisk -l
sudo dmidecode -t memory
sudo dmidecode -t system
sudo dmidecode -t bios 
sudo dmidecode -t processor 

#!/usr/bin/env bash

## install proxmox 
sudo yum install wget 
wget http://download.proxmox.com/iso/proxmox-ve_7.1-2.iso 
sudo mkdir /mnt/proxmox
sudo mount -o loop proxmox-ve_7.1-2.iso /mnt/proxmox


