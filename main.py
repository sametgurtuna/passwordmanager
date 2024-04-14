from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self,path):
        self.key = Fernet.generate_key()
        with open(path, "wb") as f:
            f.write(self.key)


    def load_key(self,path):
        with open(path, "rb") as f:
            self.key = f.read()

    def create_password_file(self,path,initial_values = None):
        self.password_file = path

        if initial_values is not None:
            for key,values in initial_values.items():
                self.add_password(key,values)


    def load_password_file(self,path):
        self.password_file = path

        with open(path, "r") as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()


    def add_password(self,site,password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, "a+") as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")


    def get_password(self,site):
        return self.password_dict[site]

    def remove_password(self, site):
        if site in self.password_dict:
            del self.password_dict[site]
            if self.password_file is not None:
                with open(self.password_file, "w") as f:
                    for s, password in self.password_dict.items():
                        encrypted = Fernet(self.key).encrypt(password.encode())
                        f.write(s + ":" + encrypted.decode() + "\n")
            print(f"Password for {site} removed successfully.")
        else:
            print(f"No password found for {site}.")


def main():
    password = {
        "email" : "123467",
        "facebook": "myfbpassword",
        "github": "mygithubpassword",
        "linkedin": "mylinkedinpassword",

    }

    pm = PasswordManager()

    pm.load_key("testkey.key")
    pm.load_password_file("mypasswords.pass")

    print("""What do you want to do?
    (1) Add a new password
    (2) Get a password
    (3) Remove a password
    (q) Quit
    """) #(1) Create a new key (2) Load an existing key (3) Create new password file (4) Load existing password file

    done = False

    while not done:
        choice = input("Enter your choice: ")
        # if choice == "1":
        #     path = input("Enter path: ")
        #     pm.create_key(path)
        # elif choice == "2":
        #     path = input("Enter path: ")
        #     pm.load_key(path)
        # elif choice == "3":
        #     path = input("Enter path: ")
        #     pm.create_password_file(path,password)
        # elif choice == "4":
        #     path = input("Enter path: ")
        #     pm.load_password_file(path)
        if choice == "1":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site,password)
        elif choice == "2":
            site = input("What site do you want: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "3":
            site = input("Enter the site you want to remove the password for: ")
            pm.remove_password(site)
        elif choice == "q":
            done = True
            print("Bye!")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()