import subprocess
import sys
import eel

eel.init("www")

# Path to Edge executable (adjust if needed)
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Start Edge in app mode pointing to the local eel server
edge_process = subprocess.Popen([
    edge_path,
    '--app=http://localhost:8000/index.html'
])

@eel.expose
def close_app():
    print("Closing app...")
    # Terminate Edge process if still running
    if edge_process.poll() is None:
        edge_process.terminate()
    # Exit Python script
    sys.exit()

# Start eel server on port 8000 without auto-opening browser
eel.start('index.html', mode=None, host='localhost', port=8000, block=True)
