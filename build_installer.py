import os
import subprocess
import sys

def create_desktop_app_bundle():
    print("=" * 60)
    print("   NESTORA DESKTOP SOFTWARE PACKAGER (EXE BUILDER)")
    print("=" * 60)
    
    # Check if pyinstaller is installed
    try:
        import PyInstaller
        print("[CHECK]: PyInstaller is already installed.")
    except ImportError:
        print("[INSTALLING]: PyInstaller required to build standalone .exe package...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Ensure nestora_desktop_app.py exists
    script_name = "nestora_desktop_app.py"
    if not os.path.exists(script_name):
        print(f"[ERROR]: {script_name} not found in current directory! Please make sure it is saved.")
        return

    print("\n[BUILDING]: Packaging Python server and UI into a standalone Windows .exe...")
    cmd = [
        "pyinstaller",
        "--onefile",
        "--noconsole",
        "--name=NestoraApp",
        script_name
    ]
    
    try:
        subprocess.check_call(cmd)
        print("\n" + "=" * 60)
        print("   BUILD SUCCESSFUL! 🎉")
        print("=" * 60)
        print("Your standalone desktop software is ready inside the 'dist' folder:")
        print("👉 Path: dist/NestoraApp.exe")
        print("\nYou can now double-click 'NestoraApp.exe' to run it like any desktop software!")
    except Exception as e:
        print(f"[BUILD ERROR]: {e}")

if __name__ == '__main__':
    create_desktop_app_bundle()

eof

### Ab kya karein?
1. Is code ko **`build_installer.py`** mein save karne ke baad terminal mein dobara yeh command run karein:
   ```powershell
   python build_installer.py
   ```
2. Jaise hi build complete ho, `dist` folder mein jakar **`NestoraApp.exe`** ko run karein!