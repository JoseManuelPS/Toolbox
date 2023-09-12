#!/bin/bash

# Force logout
date +"[%d-%m-%y %H:%M] " >> /tmp/nordvpn_mesh_autoconnecto.log; nordvpn logout --persist-token >> /tmp/nordvpn_mesh_autoconnecto.log

# Renew session
date +"[%d-%m-%y %H:%M] " >> /tmp/nordvpn_mesh_autoconnecto.log; nordvpn login --token <(token)> >> /tmp/nordvpn_mesh_autoconnecto.log

# Restart mesh setup
date +"[%d-%m-%y %H:%M] " >> /tmp/nordvpn_mesh_autoconnecto.log; nordvpn set mesh enabled >> /tmp/nordvpn_mesh_autoconnecto.log

