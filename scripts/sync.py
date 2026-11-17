#!/usr/bin/env python3
"""Synchronize upstream RoscomVPN DEFAULT profiles preserving DNS overlay."""
import base64
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]
UPSTREAM="https://raw.githubusercontent.com/hydraponique/roscomvpn-routing/main"
CLIENTS={"HAPP":"happ","INCY":"incy"}
REQUIRED={"DirectSites","DirectIp","ProxySites","ProxyIp","BlockSites","BlockIp","Geoipurl","Geositeurl","RouteOrder"}

def download(client):
    req=Request(f"{UPSTREAM}/{client}/DEFAULT.JSON",headers={"User-Agent":"GlobalHyperMegaNet-sync"})
    with urlopen(req,timeout=30) as response:
        data=json.load(response)
    if not isinstance(data,dict) or not REQUIRED.issubset(data):
        raise ValueError(f"Unexpected upstream profile: {client}")
    for key in ("DirectSites","DirectIp","ProxySites","ProxyIp","BlockSites","BlockIp"):
        if not isinstance(data[key],list):
            raise ValueError(f"Invalid {client} field: {key}")
    data.update({
        "Name":"GlobalHyperMegaNet",
        "GlobalProxy":"true",
        "RemoteDns":"94.140.14.14",
        "RemoteDNSType":"DoH",
        "RemoteDNSDomain":"https://dns.adguard-dns.com/dns-query",
        "RemoteDNSIP":"94.140.14.14",
        "DomesticDns":"77.88.8.8",
        "DomesticDNSType":"DoH",
        "DomesticDNSDomain":"https://77.88.8.8/dns-query",
        "DomesticDNSIP":"77.88.8.8",
    })
    return data

def main():
    profiles={client:download(client) for client in CLIENTS}
    for client,scheme in CLIENTS.items():
        profile=profiles[client]
        serial=json.dumps(profile,ensure_ascii=False,separators=(",",":"))
        folder=ROOT/client
        folder.mkdir(exist_ok=True)
        (folder/"DEFAULT.JSON").write_text(json.dumps(profile,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        encoded=base64.urlsafe_b64encode(serial.encode("utf-8")).decode("ascii").rstrip("=")
        (folder/"DEFAULT.DEEPLINK").write_text(f"{scheme}://routing/onadd/{encoded}\n",encoding="utf-8")
        print(f"{client}: updated")
if __name__=="__main__":
    main()
