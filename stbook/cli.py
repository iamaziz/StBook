import subprocess
import os

def run_app():
    # Get the directory where the package is installed
    dir_path = os.path.dirname(os.path.realpath(__file__))
    app_path = os.path.join(dir_path, '../app.py')

    try:
        subprocess.run(["streamlit", "run", app_path])
    except KeyboardInterrupt:
       print("Shutting down the Streamlit app...")
       exit(0)