import os
import datetime
import shutil
import glob
import extractor2


def organize_by_extension(dir):
    for file in os.listdir(dir):
        if not file.startswith('.'):
            ext = os.path.splitext(file)[1][1:].strip().lower()
            if os.path.isdir(file) or not ext:
                continue
            sub_dir = os.path.join(dir, ext)
            if not os.path.exists(sub_dir):
                os.makedirs(sub_dir)
                
            # move the file to the subdirectory
            source_file_path = os.path.join(dir, file)
            dest_file_path = os.path.join(dir, sub_dir)
            shutil.move(source_file_path, dest_file_path) 
            
def organize_files(dir):
    for file in os.listdir(dir):
        filepath = os.path.join(dir, file)
        
        modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
        date_formatted = modified_date.strftime('%B-%Y')
        
        folder_path = os.path.join(dir, date_formatted)
        try:
            os.makedirs(folder_path, exist_ok=True)
            if not file == os.path.basename(__file__):
                shutil.move(file, folder_path)
            print(f'Sucesss')
        except Exception as e:
            print(f'Error --> {e}')
            
            
        organize_by_extension(folder_path)
        

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))    
    organize_files(current_dir)
   