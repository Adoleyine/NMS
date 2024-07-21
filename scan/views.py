from django.shortcuts import render
from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup, VendorNotFoundError
# Create your views here.

def get_available_devices(target_ip):
    arp_request = ARP(pdst=target_ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    response_list = srp(arp_request_broadcast, timeout=3, verbose=False)[0]

    devices = []

    for sent, received in response_list:
        devices.append(
            {'ip': received.psrc, 'mac': received.hwsrc}
        )
    return devices


def get_vendor(mac):
    maclookup = MacLookup()
    try:
        vendor = maclookup.lookup(mac)
    except VendorNotFoundError:
        vendor = 'Unknown Vendor'
    return vendor

def dashboard(request):
    return render(request, 'base.html')

def scan_network(request):
    return render(request, 'scan/scan.html')