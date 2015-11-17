# These and other macros are documented in ../droid-configs-device/droid-configs.inc

%define device coconut
%define vendor semc

%define vendor_pretty Sony Ericsson
%define device_pretty Live with Walkman

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 0.5926

# We assume most devices will
%define have_modem 1

%define exclude_files \
/etc/dconf/db/vendor.d/jolla-camera-hw-anzu.txt\
/etc/dconf/db/vendor.d/jolla-camera-hw-haida.txt\
/etc/dconf/db/vendor.d/jolla-camera-hw-hallon.txt\
/etc/dconf/db/vendor.d/jolla-camera-hw-iyokan.txt\
/etc/dconf/db/vendor.d/jolla-camera-hw-mango.txt\
/etc/dconf/db/vendor.d/jolla-camera-hw-satsuma.txt\
/etc/dconf/db/vendor.d/jolla-camera-hw-smultron.txt\
/etc/dconf/db/vendor.d/jolla-camera-hw-urushi.txt\
%{nil}

Provides: sensord-configs

%include droid-configs-device/droid-configs.inc
