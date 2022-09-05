# from datetime import datetime
# import os
# import sys
# import subprocess as sp
# import shutil
# from time import strftime


# #UNITY_EDITOR_PATH = r"E:\Program Files\Unity Editors\2020.3.30f1\Editor\Unity.exe"
# UNITY_EDITOR_PATH = r"E:\Program Files\Unity Editors\2021.2.11f1\Editor\Unity.exe"
# #PROJECT_PATH = r"E:\repo\ci-test"
# PROJECT_PATH = r"D:\repos\galaxy_studio_new"
# LOG_PATH = r"E:\mylog.txt"
# OUTPUT_PATH = f'{PROJECT_PATH}\output\win64\galaxy_studio\galaxy_studio.exe'

# args = [
#     UNITY_EDITOR_PATH,
#     f'-logfile',
#     f'{LOG_PATH}',
#     f'-ProjectPath',
#     f'{PROJECT_PATH}',
#     f'-quit',
#     f'-batchmode',
#     f'-executeMethod',
#     f'Builder.BuildFromCI',
#     f'-outputPath',
#     f'{OUTPUT_PATH}'
# ]


# def build_win64():
#     print("sp call args: ", args)
#     r = sp.call(args)
#     if r != 0:
#         print("return code not zero, print log file content --->")
#         print_log()
#         exit(r)
#     else:
#         print_log()


# def main():
#     print("python call build begin")
#     build_win64()
#     make_archive()
#     print("python call build end")


# def print_log():
#     if not os.path.exists(LOG_PATH):
#         print(f'log file at {LOG_PATH} not exist .. return')
#     else:
#         with open(LOG_PATH, 'r', encoding='utf-8') as f:
#             n = 1
#             l = f.readline()
#             while l:
#                 sys.stdout.write(f'[Unity-Log-File-Output]:{n} {l}')
#                 n += 1
#                 l = f.readline()
#         print("\nprint log file finished\n")


# def make_archive():
#     if not os.path.exists(OUTPUT_PATH):
#         print(f'output path not exist! {OUTPUT_PATH}')
#         exit(1)

#     abspath = os.path.abspath(OUTPUT_PATH)
#     dirname = os.path.dirname(abspath)
#     zippath = shutil.make_archive('galaxy_studio', "zip", dirname)
#     build_number = os.environ.get("BUILD_NUMBER")
#     job_name = os.environ.get("JOB_NAME")
#     if not build_number:
#         print(f'no BUILD_NUMBER in env')
#         exit(1)
#     if not job_name:
#         print(f'no JOB_NAME in env')
#         exit(1)

#     path = f'./build/{job_name}/zipfile/{build_number}'
#     if not os.path.exists(path):
#         os.makedirs(path)
#     shutil.move(zippath, path)


# if __name__ == "__main__":
#     main()
