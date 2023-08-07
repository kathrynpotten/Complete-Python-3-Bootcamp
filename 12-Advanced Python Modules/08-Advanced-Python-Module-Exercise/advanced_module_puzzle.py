import shutil
import os
import re


# shutil.unpack_archive("unzip_me_for_instructions.zip", "instructions", "zip")


path = "C:/Users/kathr/OneDrive/dev/Complete-Python-3-Bootcamp/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/instructions/extracted_content"
for folder, sub_folders, files in os.walk(path):
    for file in files:
        with open(folder + "/" + file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            pattern = r"\d{3}-\d{3}-\d{4}"
            phone_number = re.findall(pattern, line)
            if phone_number != []:
                print(f"The phone number is in {folder}")
                print(phone_number[0])
