import os
from llama_cpp import Llama
from pyfiglet import Figlet
from colorama import Style, Fore, Back
from config import *

def start():
    os.system("@echo off")
    os.system("title OpenGPT")
    os.system("cls")
    print(Fore.GREEN + pyfiglet.figlet_format("OpenGPT", font="slant") + Style.RESET_ALL)
    print(Fore.YELLOW + "by Sodium | Version: 1.0 Beta\n\n" + Style.RESET_ALL)


llm = Llama(
    model_path=model_path,
    n_ctx=16000,
    n_threads=32,
    n_gpu_layers=0
)

generation_kwargs = {
    "max_tokens":20000,
    "stop":["</s>"],
    "echo":False,
    "top_k":1
}

start()
while True:
    prompt = input("$ " + Fore.GREEN)

    if prompt == "cls":
        start()
    elif prompt == "exit" or prompt == "quit":
        sys.exit()
    elif prompt == None:
        continue
    else:
        print(Style.RESET_ALL)
        res = llm(prompt, **generation_kwargs)

        print(Fore.RED + "<OpenGPT> " + Style.RESET_ALL + res["choices"][0]["text"])
