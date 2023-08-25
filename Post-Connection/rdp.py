import subprocess

def enable_rdp():
    try:
        # Enable Remote Desktop
        subprocess.run(['reg', 'add', 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server', '/v', 'fDenyTSConnections', '/t', 'REG_DWORD', '/d', '0', '/f'])
        
        # Allow RDP through the firewall
        subprocess.run(['netsh', 'advfirewall', 'firewall', 'set', 'rule', 'group="Remote Desktop"', 'new', 'enable=yes'])
        
        print("Remote Desktop has been enabled.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    enable_rdp()
