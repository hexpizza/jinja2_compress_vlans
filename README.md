# Ansible Jinja2 filter to compress vlans
This filter creates appropriate vlan list to be used in network automation.

## Description
It was made for Ansible automation using jinja2 templates.
There should be a list of vlans as strings as input, for example:
```
['1', '2', '3', '5', '7', '8', '23', '34', '56', '2', '3', '4']
```
It creates a list of compressed vlans like this one:
```
['1-3', '5', '7-8', '23', '34', '56', '3-4']
```

## Installation and usage
To install download the repository and put the script compress_vlans.py to 'filter_plugins' folder at the playbook place or to a global filter path as it's written in the Ansible [doc](https://docs.ansible.com/ansible/latest/plugins/filter.html#using-filter-plugins).

To use filter create a construction similar to: 
```
{{ vlans|compress_vlans}}
```
