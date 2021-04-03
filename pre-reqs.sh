yum -y install wget

echo "Creating filesystem for data"
mkfs.xfs -f /dev/sdb
echo "`blkid|grep sdb|awk '{print $2'}` /data              xfs    defaults        0 0" >> /etc/fstab
mount /data

echo "Opening 80 and 8850 ports..."
firewall-cmd --permanent --add-port=80/tcp
firewall-cmd --permanent --add-port=8850/tcp
systemctl restart firewalld

#echo "Donwloading config files..."
#git clone https://github.com/abondili51/TS-Auto.git /tmp/ts-auto
