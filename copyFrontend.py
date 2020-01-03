import os,shutil

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            if os.path.exists(d):
                shutil.copy2(s, d)
            else:
                print("Can not delete the file as it doesn't exists")
                shutil.copy2(s, d)

shutil.rmtree('apilogin/login/templates')
os.mkdir('apilogin/login/templates')
copytree('frontend/target/dist/','apilogin/login/templates')
print("Done")
