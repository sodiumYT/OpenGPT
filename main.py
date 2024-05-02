import os
import tkinter as tk
from tkinter import ttk, filedialog
from llama_cpp import Llama
import pyfiglet
from colorama import Style, Fore, Back

def start():
    os.system("@echo off")
    os.system("title OpenGPT")
    os.system("cls")
    print(Fore.GREEN + pyfiglet.figlet_format("OpenGPT", font="slant") + Style.RESET_ALL)
    print(Fore.YELLOW + "by Sodium | Version: 1.0 Beta\n\n" + Style.RESET_ALL)

def browse_file():
    filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Model File", filetypes=(("Model files", "*.gguf"), ("All files", "*.*")))
    if filepath:
        model_path_var.set(filepath)

def send_message():
    message = entry.get()
    if message.strip() != "":
        conversation.config(state=tk.NORMAL)
        conversation.insert(tk.END, "$ " + message + "\n\n", "user")
        response = generate_response(message)
        conversation.insert(tk.END, "<OpenGPT> " + response + "\n\n", "bot")
        conversation.see(tk.END)
        entry.delete(0, tk.END)

def generate_response(prompt):
    llm = Llama(
        model_path=model_path_var.get(),
        n_ctx=16000,
        n_threads=32,
        n_gpu_layers=0
    )
    res = llm(prompt, **generation_kwargs)
    return res["choices"][0]["text"]

generation_kwargs = {
    "max_tokens":20000,
    "stop":["</s>"],
    "echo":False,
    "top_k":1
}

root = tk.Tk()
root.title("OpenGPT Chat")

# Tab control
tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill="both")

# Chat tab
chat_tab = ttk.Frame(tab_control)
tab_control.add(chat_tab, text="Chat")

conversation = tk.Text(chat_tab, wrap=tk.WORD, state=tk.DISABLED)
conversation.tag_config("user", foreground="green")
conversation.tag_config("bot", foreground="red")
conversation.pack(expand=True, fill=tk.BOTH)

entry_frame = tk.Frame(chat_tab)
entry_frame.pack(side=tk.BOTTOM, fill=tk.X)
entry = tk.Entry(entry_frame)
entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
entry.bind("<Return>", lambda event: send_message())
send_button = tk.Button(entry_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

# Settings tab
settings_tab = ttk.Frame(tab_control)
tab_control.add(settings_tab, text="Settings")

model_path_label = tk.Label(settings_tab, text="Model Path:")
model_path_label.pack()

model_path_var = tk.StringVar()
model_path_entry = tk.Entry(settings_tab, textvariable=model_path_var)
model_path_entry.pack(side=tk.LEFT)

browse_button = tk.Button(settings_tab, text="Browse", command=browse_file)
browse_button.pack(side=tk.RIGHT)

start()
input()

root.mainloop()
