import os
import sys
import base64

def run_os_cmd(cmd, msg):
    print("\n")
    print(msg)
    os.system(cmd)

def run_pre_reqs():
    yum_cmd='sudo yum -y install wget'
    run_os_cmd(yum_cmd,"Installing wget...")

    fw_cmd1='sudo firewall-cmd --permanent --add-port=80/tcp'
    fw_cmd2='sudo firewall-cmd --permanent --add-port=8850/tcp'
    fw_cmd3='sudo systemctl restart firewalld'
    run_os_cmd(fw_cmd1,"Opening port 80...")
    run_os_cmd(fw_cmd2,"Opening port 8850...")
    run_os_cmd(fw_cmd3,"Restarting firewalld...")


def download_install():    
    download_cmd='wget https://downloads.tableau.com/esdalt/2021.2.8/tableau-server-2021-2-8.x86_64.rpm -P /tmp'
    run_os_cmd(download_cmd,'Downloading Tableau Server Package...')

    install_cmd='yum -y install /tmp/tableau-server-2021-2-8.x86_64.rpm'
    run_os_cmd(install_cmd,'Installing Package...')

def initialize():
    initialize_cmd='sudo /opt/tableau/tableau_server/packages/scripts.2021*/initialize-tsm -f --accepteula -a aravind.bondili'
    run_os_cmd(initialize_cmd,'Initializing TSM...')
    sourcing_cmd='source /etc/profile.d/tableau_server.sh'
    run_os_cmd(sourcing_cmd,'Sourcing tableau profile...')

def activate_register():
    license_cmd='sudo /opt/tableau/tableau_server/packages/customer-bin.20*/tsm licenses activate -t'
    run_os_cmd(license_cmd,'Activating Trial License...')

    register_cmd='sudo /opt/tableau/tableau_server/packages/customer-bin.20*/tsm register --file /tmp/ts-auto/config/register.json'
    run_os_cmd(register_cmd,'Registratering...')

def configure():
    id_store_cmd='sudo /opt/tableau/tableau_server/packages/customer-bin.20*/tsm settings import -f /tmp/ts-auto/config/id_store.json'
    run_os_cmd(id_store_cmd,'Configuring ID store settings...')

    apply_changes='sudo /opt/tableau/tableau_server/packages/customer-bin.20*/tsm pending-changes apply'
    run_os_cmd(apply_changes,'Applying pending changes...')

def start_ts():
    start_ts='sudo /opt/tableau/tableau_server/packages/customer-bin.20*/tsm initialize --start-server --request-timeout 1800'
    run_os_cmd(start_ts,'Initializing and Starting Tableau Server...')

def add_admin():
    pwd=base64.b64decode('YWRtaW4=').decode()
    add_admin=f"sudo /opt/tableau/tableau_server/packages/customer-bin.20*/tabcmd initialuser --server http://localhost --username 'admin' --password {pwd}"
    run_os_cmd(add_admin,'Adding admin account...')
    print('Admin account is successfully added!')

def main():
    run_pre_reqs()
    download_install()
    initialize()
    activate_register()
    configure()
    start_ts()
    add_admin()

        
if __name__ == '__main__':
    #server = sys.argv[1] if len(sys.argv)==1 else '35.211.112.6'
    main()
