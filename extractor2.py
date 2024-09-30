import os
import shutil
 
folder = os.path.dirname(os.path.realpath(__file__))

def delete_empty_folders(root):
    deleted = set()
    
    for dir, subdirs, files in os.walk(root, topdown=False):

        still_has_subdirs = False
        for subdir in subdirs:
            if os.path.join(dir, subdir) not in deleted:
                still_has_subdirs = True
                break
    
        if not any(files) and not still_has_subdirs:
            os.rmdir(dir)
            deleted.add(dir)
            
    return deleted
  
def extract(dir):
    _dirs = []
    
    for root, dirs, files in os.walk(dir):
        _dirs.append(dirs)
        for root, dirs, files in os.walk(dir, topdown=False):
                for f in files:
                    src =  os.path.join(root, f)
                    dst = os.path.join(folder, f)
                    shutil.move(src, dst)   
            
                for dirname in dirnames:
                    full_path = os.path.join(root, dirname)
                    destination = os.path.join(folder, dirname)
                    
                    if not os.path.exists(destination):
                        try:
                           shutil.move(full_path, destination)
                        except Exception as e:
                            print('Error {e} encountered while moving file {dirname} from {full_path} to {folder}') 
                        else:
                            print('ALL FOLDERS IN {full_path} HAVE BEEN EXTRACTED')
                        # end try
                        
                    delete_empty_folders(dirnames)



                
               
    if len(_dirs) == 0:
            return
            
if __name__ == '__main__':
    extract(folder)
    
    
   