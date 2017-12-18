import platform


def windows_os():
    var = dict()

    var['os'] = platform.system()

    var['os_family'] = 'Windows'

    var['kernel'] = 'Windows'

    osrelease = platform.release()
    if osrelease == '10':
        var['osrelease'] = '2016Server'
    if osrelease == '8.1':
        var['osrelease'] = '2012ServerR2'
    if osrelease == '8':
        var['osrelease'] = '2012Server'
    if osrelease == '7':
        var['osrelease'] = '2008ServerR2'
    if osrelease == 'Vista':
        var['osrelease'] = '2008Server'

    var['osfinger'] = platform.system() + " " + var['osrelease']

    var ['osfullname'] = platform.system() + ' ' + var['osrelease'] + ' ' + platform.version()

    var['osmajorrelease'] = var['osrelease'][:4]

    return var


def ubuntu_os():
    var = dict()

    val = []

    var['os'] = platform.linux_distribution()[0]

    var['osrelease'] = platform.linux_distribution()[1]

    var['kernel'] = 'Linux'

    var['osfinger'] = var['os'] + " " + var['osrelease']

    var['os_family'] = 'Linux'

    with open('/etc/os-release', 'r') as f:
        val = [line.strip() for line in f]

    var['osfullname'] = var['os'] + " " + val[1].split("=")[1].replace('"','')

    var['osmajorrelease'] = val[5].split("=")[1].replace('"','')

    return var


def cent_os():
    var = dict()

    val = []

    var['os'] = platform.linux_distribution()[0]

    var['osrelease'] = platform.linux_distribution()[1]

    var['kernel'] = 'Linux'

    var['osfinger'] = var['os'] + " " + var['osrelease']

    var['os_family'] = 'Linux'

    with open('/etc/os-release', 'r') as f:
        val = [line.strip() for line in f]

    var['osfullname'] = var['os'] + " " + val[1].split("=")[1].replace('"','')

    var['osmajorrelease'] = val[5].split("=")[1].replace('"','')

    return var


def debian_os():
    var = dict()

    val = []

    var['os'] = platform.linux_distribution()[0]

    var['osrelease'] = platform.linux_distribution()[1]

    var['kernel'] = 'Linux'

    var['osfinger'] = var['os'] + " " + var['osrelease']

    var['os_family'] = 'Linux'

    with open('/etc/os-release', 'r') as f:
        val = [line.strip() for line in f]

    var['osfullname'] = var['os'] + " " + val[0].split("=")[1].replace('"','')

    var['osmajorrelease'] = val[4].split("=")[1].replace('"','')

    return var

def rhel_os():

    var = dict()

    val = []

    var['os'] = platform.linux_distribution()[0]

    var['osrelease'] = platform.linux_distribution()[1]

    var['kernel'] = 'Linux'

    var['osfinger'] = var['os'] + " " + var['osrelease']

    var['os_family'] = 'Linux'

    with open('/etc/os-release', 'r') as f:
        val = [line.strip() for line in f]

    var['osfullname'] = val[5].split("=")[1].replace('"', '')

    var['osmajorrelease'] = val[4].split("=")[1].replace('"', '')

    return var


if platform.system() == 'Windows':
    os_info_dict = windows_os()
else:
    if platform.linux_distribution()[0] == 'Ubuntu':
        os_info_dict = ubuntu_os()
    if platform.linux_distribution()[0] == 'CentOS Linux':
        os_info_dict = cent_os()
    if platform.linux_distribution()[0] == 'debian':
        os_info_dict = debian_os()
    if platform.linux_distribution()[0] == 'Red Hat Enterprise Linux Server':
        os_info_dict = rhel_os()

#print os_info_dict




