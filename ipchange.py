"""A script that can change static ip address or use DHCP"""
import ctypes, sys

def is_admin():
    """Check admin permission"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Change your ip and subnetmark
    import wmi
    c = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled = 1)
    nic = c[0]
    select = input("Press 1 to change static ip or 2 to use DHCP:")
    if select == "1":
        ip = input("Input your new ip address:")
        subnetmask = input("Input your subnetmark:")
        nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    elif select == "2":
        nic.EnableDHCP()
    else:
        pass
else:
    # Re-run the program with admin permission
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
