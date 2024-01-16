import subprocess
if __name__ == "__main__":
    uninstall_result = subprocess.getoutput(f'echo "jenkins" > /a.txt')