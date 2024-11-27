import logging
import os
import subprocess

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',)

def test_main():
    logging.info("Test main with EVEN Distribution")
    script_path = os.path.join("main", "main.py")
    result = subprocess.run(
        ["python", script_path, "-M3"], capture_output=True, text=True
    )

    logging.info(result.returncode)
    logging.info(result.stdout)
    logging.info(result.stdout.strip())