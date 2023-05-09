import os
import shutil

students ={
    # # "Jurgita":"",
    # "sheridan":"https://github.com/BigBird29575/shopping_cart",
    # "jeremy":"https://github.com/jermateo/shopping_cart",
    # # "desiree":"",
    # "mani":"https://github.com/MemoriesWholesale/PirateShop.git",
    # "mason":"https://github.com/masonsinner/shopping_cart_python",
    # "leisa":"https://github.com/leisatrisler/wk2-python-basics-project",
    # "Val":"https://github.com/ValenciaW9/PythonShoppingCart.git",
    # # "keanu":"",
    # # "austin":"",
    # "Cyn":"https://github.com/Melikrome1/shoppingcart/blob/main/Untitled.ipynb" 
}



for name, url in students.items():
    os.system(f"git clone {url} {name}")
    if os.path.isfile("./.env"):
        shutil.copyfile("./.env", f"./{name}/.env")
        print(name)
        os.chdir(f"{name}")
        if os.path.isdir("./migrations"):
            print("here")
            shutil.rmtree('migrations')
        os.system(f". ../flask-load.sh")
        os.chdir(f"..")
    if os.path.isfile(f"./{name}/package.json"):
        os.chdir(f"{name}")
        os.system("npm install")
        os.chdir(f"..")
