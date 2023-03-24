import os
import shutil

students ={
    "John-react":"https://github.com/CrtlAltElite/CRAVE",
}



for name, url in students.items():
    os.system(f"git clone {url} {name}")
    if os.path.isfile("./.env"):
        shutil.copyfile("./.env", f"./{name}/.env")
        os.chdir(f"{name}")
        os.system(f". ../flask-load.sh")
        os.chdir(f"..")
    if os.path.isfile(f"./{name}/package.json"):
        os.chdir(f"{name}")
        os.system("npm install")
        os.chdir(f"..")
