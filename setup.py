from config import helper

if __name__ == "__main__":
    print(f"\n[+] Setting up application...\n")
    if helper.rename_config_file() == True:
        print(f"[+] Success!\n")
    else:
        print(f"[-] Cannot setup the application!\n")
        print(f"[-] ERROR: {helper.rename_config_file()}")