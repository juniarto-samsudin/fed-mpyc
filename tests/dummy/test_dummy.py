from modules.dummy.operations import add, subtract
import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',)

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_launch_process():
    # Launch the script as a process
    script_path = os.path.join("tests/dummy", "script.py")
    result = subprocess.run(
        ["python", script_path], capture_output=True, text=True
    )

    # Assert the output
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello from script.py!"

def test_launch_mpc():
    # Launch the script as a process
    script_path = os.path.join("tests/dummy", "simplempc.py")
    result = subprocess.run(
        ["python", script_path, "-M3"], capture_output=True, text=True
    )
    logging.info(result.returncode)
    logging.info(result.stdout)
    logging.info(result.stdout.strip())
    
    # Assert the output
    assert result.returncode == 0
    #assert result.stdout.strip() == "Hello from script.py!"
