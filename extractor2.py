import os
import shutil
 
folder = os.path.dirname(os.path.realpath(__file__))
  
def extract(dir):
    _dirs = []
    
    for root, dirs, files in os.walk(dir):
        _dirs.append(dirs)
        for f in files:
            src =  os.path.join(root, f)
            dst = os.path.join(folder, f)
            shutil.move(src, dst)
            
        for d in dirs:
            src =  os.path.join(root, d)
            dst = os.path.join(folder, d)
            
            if not os.path.exists(dst):
                try:
                    shutil.move(src, dst)
                except Exception as e:
                    print('Error {e} encountered') 
                
               
    if len(_dirs) == 0:
            return
            
if __name__ == '__main__':
    extract(folder)
    