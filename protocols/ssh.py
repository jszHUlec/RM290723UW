import paramiko

sshClient = paramiko.SSHClient()

sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshClient.load_system_host_keys()

sshClient.connect(hostname="10.0.3.12",port=22,username="kali",password="kali")

while True:
    komenda = input("komenda: ")
    if komenda == "exit":
        break
    stdin, stdout, stderr = sshClient.exec_command(komenda)
    print(stdout.read().decode("UTF-8"))
    # print(stderr.read().decode("UTF-8"))

sshClient.close()