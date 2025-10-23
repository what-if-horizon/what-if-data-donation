"""
To run this script: python3 structure_donations/structure_parsers.py
All python files are executed in parallel using multithreading
"""
import threading
import subprocess

py_scripts = ['YT_csv_to_csv.py',
'YT_json_to_csv.py',
'TT_json_to_csv.py',
'X_json_to_csv.py',
'IG_json_to_csv.py',
'FB_json_to_csv.py']

main_path = 'structure_donations/Parser_structures_to_merged_structures/'

def run_script(script_name):
    subprocess.run(["python3", script_name])

if __name__ == "__main__":

    threads = []

    for p in py_scripts: 
        path = f'{main_path}/{p}'
        thread = threading.Thread(target=run_script, args=(path,))
        threads.append(thread)


    for t in threads:
        t.start()

    for t in threads:
        t.join()

    
    print("ALL scripts have finished executing")

