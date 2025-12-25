from scapy.all import sniff,ARP,IP
import time

alive_hosts=set()

def packet_callback(packet):
    ip=None
    if packet.hsalayer(ARP): #check Arp packet,the packet must be ARP
        ip=packet[ARP].psrc #get ip address
        mac=packet[ARP].hwsrc #get mac address
    elif packet.hsalayer(IP): #check IP packet,the packet must be IP
        ip=packet[IP].src
    
    if ip and ip not in alive_hosts: #can not found any ip in live host
        alive_hosts.add(ip)
        print(f"[发现新主机] IP:{ip} | 时间：{time.strftime('%H:%M:%S')}")

def start_passive_scan(interface=None,timeout=60):
    #start passive scan
    #interface:name of netcard
    #timeout:Maximum time to wait for packets
    print(f"[*]将位于接口{interface}启动被动监听....预计等待时间{timeout}秒")
    print("-"*60)

    try:
        sniff(  
            iface=interface,   #it's used to found packet
            filter="arp or ip",  #means to catch arp or icmp or ip packet
            prn=packet_callback,    #rollback function,if cathc a packet,it will be rollback
            timeout=timeout,    #the catch packet will not be saved
            store=0
        )
    except PermissionError:
        print("[*]请以管理员权限运行程序")
    except Exception as e:
        print(f"未能监听,因为{e}")
    print("-"*60)
    print(f"[*]已结束监听,已找到{len(alive_hosts)}个主机")
    print("存活主机列表:",sorted(alive_hosts))

if __name__=="__main__":
    start_passive_scan(interface=None,timeout=30)

#this program run in lay2,need Wincap devier to run
#User must install Npcap first,and use scapy model in python
#https://nmap.org/npcap/
#instyall scapy: pip install scapy
