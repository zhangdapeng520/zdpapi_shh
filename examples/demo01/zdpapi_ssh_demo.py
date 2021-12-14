from zdpapi_ssh import SSH

ssh = SSH(hostname='192.168.18.11', port=22,
          username='zhangdapeng', password='zhangdapeng')
ssh.execute('df -hl')
