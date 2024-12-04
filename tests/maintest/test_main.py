import logging
import os
import subprocess

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',)

def basic_info():
    logging.info('Alice:   [[1,2]')
    logging.info('          [3,4]]')
    logging.info('Bob:     [[5,6]')
    logging.info('          [7,8]]')
    logging.info('Charlie: [[9,10]')
    logging.info('          [11,12]]')
def test_sum_column0():
    logging.info("Test SUM of COLUMN 0 with EVEN Distribution")
    basic_info()
    script_path = os.path.join("main", "main.py")
    result = subprocess.run(
        ["python", script_path,"--input_request", '{"columnNo":0, "aggregator":"SUM"}', "-M3"], capture_output=True, text=True
    )
    
    logging.info(result.returncode)
    logging.info(result.stdout.strip())
    assert result.returncode == 0

def test_sum_column1():
    logging.info("Test SUM of COLUMN 1 with EVEN Distribution")
    basic_info()
    script_path = os.path.join("main", "main.py")
    result = subprocess.run(
        ["python", script_path,"--input_request", '{"columnNo":1, "aggregator":"SUM"}', "-M3"], capture_output=True, text=True
    )

    logging.info(result.returncode)
    logging.info(result.stdout.strip())
    assert result.returncode == 0

def test_count():
    logging.info("Test COUNT of COLUMN 0 with EVEN Distribution")
    basic_info()
    script_path = os.path.join("main", "main.py")
    result = subprocess.run(
        ["python", script_path,"--input_request", '{"columnNo":0, "aggregator":"COUNT"}', "-M3"], capture_output=True, text=True
    )
    logging.info(result.returncode)
    logging.info(result.stdout.strip())
    assert result.returncode == 0

def test_max():
    logging.info("Test MAX of COLUMN 1 with EVEN Distribution")
    basic_info()
    script_path = os.path.join("main", "main.py")
    result = subprocess.run(
        ["python", script_path,"--input_request", '{"columnNo":0, "aggregator":"MAX"}', "-M3"], capture_output=True, text=True
    )
    logging.info(result.returncode)
    logging.info(result.stdout.strip())
    assert result.returncode == 0

def test_min():
    logging.info("Test MIN of COLUMN 1 with EVEN Distribution")
    basic_info()
    script_path = os.path.join("main", "main.py")
    result = subprocess.run(
        ["python", script_path,"--input_request", '{"columnNo":0, "aggregator":"MIN"}', "-M3"], capture_output=True, text=True
    )
    logging.info(result.returncode)
    logging.info(result.stdout.strip())
    assert result.returncode == 0