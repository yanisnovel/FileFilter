import os
import shutil

repertory =  "C:/Users/..."

#Put your folder here but not with \ but wiith / example :
# C:\Users\..  NO
# C:/Users/../... YES !


EXTENSIONS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Executables': ['.exe', '.msi', '.dmg']
}

def organisateur(repertory):
    result = ""

    if not os.path.exists(repertory):
        result = f"Error: No '{repertory}' folder was found."
    else:
        counter = 0
        for i in os.listdir(repertory):
            path = os.path.join(repertory, i)

            if os.path.isfile(path):
                name, ext = os.path.splitext(i)
                ext = ext.lower()

                categories = "Autres"
                for cat, liste_ext in EXTENSIONS.items():
                    if ext in liste_ext:
                        categories = cat
                        break 
                # ------------------------------------------

                dest = os.path.join(repertory, categories)
                if not os.path.exists(dest):
                    os.makedirs(dest)
                
  
                shutil.move(path, os.path.join(dest, i))
                counter += 1
        
        result = f"Success: {counter} files have been organized."

    return result

if __name__ == "__main__":
    print(organisateur(repertory))