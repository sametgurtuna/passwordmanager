import tkinter as tk
from tkinter import simpledialog, messagebox
from cryptography.fernet import Fernet
import clipboard

class PasswordManagerGUI:

    def __init__(self, master):
        self.master = master
        master.title("Password Manager")
        master.geometry("400x240")  # Pencere boyutu
        master.configure(bg="#f0f0f0")

        # Font stilleri
        button_font = ("Arial", 10)
        label_font = ("Arial", 12, "bold")

        self.pm = PasswordManager()
        self.pm.load_key("key.key")
        self.pm.load_password_file("passwords.pass")

        self.label = tk.Label(master, text="What do you want to do?", font=label_font, bg="#f0f0f0")
        self.label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        # Butonların oluşturulması ve düzenlenmesi
        buttons = [
            ("Create a new key", self.create_key),
            ("Load an existing key", self.load_key),
            ("Add a new password", self.add_password),
            ("Get a password", self.get_password),
            ("Remove a password", self.remove_password),
            ("Quit", master.quit)
        ]

        for i, (text, command) in enumerate(buttons):
            button = tk.Button(master, text=text, width=15, command=command, font=button_font, bg="#007bff", fg="white", relief="raised")
            if i < 3:
                button.grid(row=i+1, column=0, padx=(40, 20), pady=5)
            else:
                button.grid(row=i-2, column=1, padx=(20, 40), pady=5)

    def create_key(self):
        path = simpledialog.askstring("Create Key", "Enter path:")
        if path:
            self.pm.create_key(path)
            messagebox.showinfo("Success", "Key created successfully.")

    def load_key(self):
        path = simpledialog.askstring("Load Key", "Enter path:")
        if path:
            self.pm.load_key(path)
            messagebox.showinfo("Success", "Key loaded successfully.")

    def add_password(self):
        site = simpledialog.askstring("Add Password", "Enter the site:")
        password = simpledialog.askstring("Add Password", "Enter the password:")
        if site and password:
            self.pm.add_password(site, password)
            messagebox.showinfo("Success", "Password added successfully.")

    def get_password(self):
        sites = self.pm.get_password()
        if sites:
            site = simpledialog.askstring("Get Password", "Available sites:\n" + "\n".join(sites) + "\nEnter the site:")
            if site:
                password = self.pm.get_password(site)
                if password:
                    clipboard.copy(password)
                    messagebox.showinfo(site, f"Password for {site} is {password}\nPassword copied to clipboard.")
                else:
                    messagebox.showwarning("Warning", f"No password found for {site}.")
        else:
            messagebox.showwarning("Warning", "No passwords found.")

    def remove_password(self):
        sites = self.pm.get_password()
        if sites:
            site = simpledialog.askstring("Remove Password",
                                          "Available sites:\n" + "\n".join(sites) + "\nEnter the site:")
            if site:
                self.pm.remove_password(site)
                messagebox.showinfo("Success", f"Password for {site} removed successfully.")
        else:
            messagebox.showwarning("Warning", "No passwords found.")

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, "wb") as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, "rb") as f:
            self.key = f.read()

    def load_password_file(self, path):
        self.password_file = path
        try:
            with open(path, "r") as f:
                for line in f:
                    site, encrypted = line.strip().split(":")
                    decrypted = Fernet(self.key).decrypt(encrypted.encode()).decode()
                    self.password_dict[site] = decrypted
        except FileNotFoundError:
            messagebox.showwarning("Warning", "Password file not found.")

    def add_password(self, site, password):
        self.password_dict[site] = password
        if self.password_file:
            with open(self.password_file, "a") as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site=None):
        if site is None:
            return list(self.password_dict.keys())
        else:
            return self.password_dict.get(site, f"No password found for {site}.")

    def remove_password(self, site):
        if site in self.password_dict:
            del self.password_dict[site]
            if self.password_file:
                with open(self.password_file, "w") as f:
                    for s, password in self.password_dict.items():
                        encrypted = Fernet(self.key).encrypt(password.encode())
                        f.write(s + ":" + encrypted.decode() + "\n")

def main():
    root = tk.Tk()
    my_gui = PasswordManagerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
