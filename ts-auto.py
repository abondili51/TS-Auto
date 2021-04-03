import os
import base64


def run_os_cmd(cmd, msg):
    print(msg)
    os.system(cmd)

    
download_cmd='wget https://www.tableau.com/support/releases/server/2021.1 -P /tmp'
run_os_cmd(download_cmd,'Downloading Tableau Server Package...')

install_cmd='yum -y install /tmp/tableau-server*'
run_os_cmd(install_cmd,'Installing Package...')

initialize_cmd='/opt/tableau/tableau_server/packages/scripts*/initialize-tsm --accepteula -a aravind.bondili -d /data'
run_os_cmd(initialize_cmd,'Initializing TSM...')
run_os_cmd('source /etc/profile.d/tableau_server.sh','Sourcing tableau profile...')

license_cmd='tsm licenses activate -t'
run_os_cmd(license_cmd,'Activating Trial License...')

register_cmd='tsm register --file /tmp/ts-auto/config/register.json'
run_os_cmd(register_cmd,'Registratering...')

id_store_cmd='tsm settings import -f /tmp/ts-auto/config/id_store.json'
run_os_cmd(id_store_cmd,'Configuring ID store settings...')

apply_changes='tsm pending-changes apply'
run_os_cmd(apply_changes,'Applying pending changes...')

start_ts='tsm initialize --start-server --request-timeout 1800'
run_os_cmd(start_ts,'Initializing and Starting Tableau Server...')

pwd=base64.b64decode('YWRtaW4=').decode()
add_admin="tabcmd initialuser --server http://localhost --username 'admin' --password %s" %pwd
run_os_cmd(add_admin,'Adding admin account...')
print('Admin account is successfully added!')
