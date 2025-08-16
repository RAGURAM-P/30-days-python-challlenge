import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Format: Hour:Minute:Second
    label.config(text=current_time)           # Update label text
    label.after(1000, update_time)            # Refresh every 1 second

# Create main window
root = tk.Tk()
root.title("⏰ Digital Clock")
root.geometry("400x200")
root.configure(bg="black")

# Create label for clock
label = tk.Label(root, font=("Helvetica", 48, "bold"), fg="cyan", bg="black")
label.pack(expand=True)

# Call update function
update_time()

# Run the GUI
root.mainloop()
