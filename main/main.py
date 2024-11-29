from mpyc.runtime import mpc
import os
import sys
import numpy as np
import logging
import argparse
import json


# Add the root directory of your project to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# If using pipenv, comment out the line above.
# pipenv shell will read .env file and add the root directory to the PYTHONPATH
from modules.mpccalc.aggregator import AggregatorHandler

#for file logging uncomment the below line
#logging.basicConfig(filename='./logs/app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', 
#                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S %p')
async def main(input_request={"columnNo": 0, "aggregator": "SUM"}):
    await mpc.start()
    secint = mpc.SecInt(32)
    if mpc.pid == 0:
        secret_table = [
            [1014386591729452595, 14708652179945530064],
            [255687502648400104, 6089180157347296504],
            [5078654821313334145, 9674100492056705436 ],
            [15740483395468817732, 16216284038025746146],
            [3310829543370176529, 11240045466950784333],
            [14960446323299013059, 153906376854957712]
        ]
    elif mpc.pid == 1:
        secret_table = [
            [2028773183458905189, 10970560286181508699],
            [511375005296800205, 12178360314694593004],
            [10157309642626668285, 901456910403859439],
            [13034222717228084030, 13985824002341940857],
            [6621659086740353049, 4033346860192017229],
            [11474148572888474680, 307812753709915412]
     ]
    elif mpc.pid == 2:
        secret_table = [
            [3043159775188357783, 7232468392417487334],
            [767062507945200306, 18267540472041889504],
            [15235964463940002425, 10575557402460564869],
            [10327962038987350328, 11755363966658135568],
            [9932488630110529569, 15273392327142801552],
            [7987850822477936301, 461719130564873112]
        ]    

    secret_table = np.array(
        [[secint(x) for x in row] for row in secret_table]
    )

    #setting chain1
    my_aggregator_handler = AggregatorHandler()

    #request 
    input_request = {'secret_table': secret_table, 
                     'columnNo': input_request.get('columnNo', 0), 
                     'aggregator': input_request.get('aggregator', 'SUM')}
    result = await my_aggregator_handler.handle(input_request)
    logging.info('Result Chain1: {}'.format(result))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run MPC with input request')
    parser.add_argument('--input_request', type=str, required=True, help='Input request as JSON string')
    args = parser.parse_args()

    input_request = json.loads(args.input_request)
    mpc.run(main(input_request))