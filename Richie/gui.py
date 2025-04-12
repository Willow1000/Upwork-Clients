import tkinter as tk
from tkinter import ttk, messagebox
from account_loader import load_accounts  # Import the load_accounts function from account_loader.py
import tkinter as tk
from automations import run_automation  # Import the run_automation function from automate_data_feed.py

accounts = load_accounts()

def on_start():
    emails = [acc['Email'] for acc in accounts]
    print(f"Loaded emails: {emails}")
    account_var = tk.StringVar(value=emails[0] if emails else None)
    selected_email = account_var.get()
    print(f"Selected email: {selected_email}")
    account = next((acc for acc in accounts if acc['Email'] == selected_email), None)

    if account:
        run_automation(account,log_box,tk=tk)
        print(f"Running automation for {account['Email']}...")
        log_box.insert(tk.END, f"Running automation for {account['Email']}...\n")


root = tk.Tk()
root.title("Automation Tool")
root.geometry("600x300")

account_var = tk.StringVar()
ttk.Label(root, text="Select Account:").pack(pady=10)
ttk.Combobox(root, textvariable=account_var, values=[acc['Email'] for acc in accounts]).pack(pady=10)
ttk.Button(root, text="Start Automation", command=on_start).pack(pady=20)

log_box = tk.Text(root, wrap=tk.WORD, height=10,width=70)
log_box.pack(pady=10)
root.mainloop()


