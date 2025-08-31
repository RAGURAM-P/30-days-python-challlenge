import tkinter as tk
from tkinter import messagebox

# Simple credentials (could be replaced with file or DB check)
USER_CREDENTIALS = {
    "admin": "1234",
    "raguram": "password"
}

def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username} 🎉")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password!")

def clear_fields():
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Login System")
root.geometry("400x250")
root.config(bg="#f4f4f4")

# Title
tk.Label(root, text="🔐 Login System", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=10)

# Username
tk.Label(root, text="Username:", font=("Arial", 12), bg="#f4f4f4").pack()
entry_user = tk.Entry(root, font=("Arial", 12))
entry_user.pack(pady=5)

# Password
tk.Label(root, text="Password:", font=("Arial", 12), bg="#f4f4f4").pack()
entry_pass = tk.Entry(root, font=("Arial", 12), show="*")
entry_pass.pack(pady=5)

# Buttons
frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=15)

btn_login = tk.Button(frame, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white",
                      width=10, command=login)
btn_login.grid(row=0, column=0, padx=5)

btn_clear = tk.Button(frame, text="Clear", font=("Arial", 12), bg="#f44336", fg="white",
                      width=10, command=clear_fields)
btn_clear.grid(row=0, column=1, padx=5)

root.mainloop()
