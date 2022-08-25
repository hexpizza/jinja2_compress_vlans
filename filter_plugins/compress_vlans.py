#!/usr/bin/venv python
def compress_vlans(vlan_list):
    """
    Convert list of strings with vlans to compressed list

    ex. ['1', '2', '3', '5', '7', '8', '23', '34', '56', '2', '3', '4']
    => ['1-3', '5', '7-8', '23', '34', '56', '3-4']
    """
    if len(vlan_list) == 0:
        return vlan_list
    for i in range(len(vlan_list)):
        vlan_list[i] = int(vlan_list[i])
    order_start = None
    order_length = None
    upgraded_vlan_list = []
    for i in range(len(vlan_list)):
        if i == 0:
            order_start = vlan_list[i]
            order_length = 1
        elif vlan_list[i] - (order_start + order_length) == 0:
            order_length += 1
            continue
        elif vlan_list[i] - order_length != 1:
            apply_order(order_start, order_length, upgraded_vlan_list)
            order_start = vlan_list[i]
            order_length = 1
    apply_order(order_start, order_length, upgraded_vlan_list)
    return upgraded_vlan_list


def apply_order(order_start, order_length, upgraded_vlan_list):
    """
    Apply range of vlans to a new list
    """
    if order_length == 1:
        upgraded_vlan_list.append(str(order_start))
    else:
        upgraded_vlan_list.append(
            str(order_start) + '-' + str(order_start + order_length - 1)
        )


class FilterModule(object):
    """
    Custom jinja2 filters to convert vlan list
    """

    def filters(self):
        return {
            'compress_vlans': compress_vlans
        }
