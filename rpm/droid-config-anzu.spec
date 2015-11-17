# These and other macros are documented in ../droid-configs-device/droid-configs.inc

%define device anzu
%define vendor semc

%define vendor_pretty Sony Ericsson
%define device_pretty Xperia Arc

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 0.88889

# We assume most devices will
%define have_modem 1

%define exclude_files \
/etc/dconf/db/vendor.d/jolla-camera-hw-(coconut|haida|hallon|iyokan|mango|satsuma|smultron|urushi).txt\
%{nil}

Provides: sensord-configs

%include droid-configs-device/droid-configs.inc
