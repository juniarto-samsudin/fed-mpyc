from mpyc.runtime import mpc
import os
import sys
import numpy as np
import logging


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
async def main():
    await mpc.start()
    secint = mpc.SecInt(32)
    if mpc.pid == 0:
        secret_table = [
        [(1014386591729452595, 5078654821313334145, 3310829543370176529),(14708652179945530064, 9674100492056705436, 11240045466950784333  )],
        [(255687502648400104, 15740483395468817732,14960446323299013059),(6089180157347296504,16216284038025746146, 153906376854957712  )]
        ]
    elif mpc.pid == 1:
        secret_table = [
        [(2028773183458905189, 10157309642626668285, 6621659086740353049  ),(10970560286181508699,901456910403859439,4033346860192017229  )],
        [(511375005296800205,13034222717228084030, 11474148572888474680  ),(12178360314694593004,13985824002341940857, 307812753709915412  )]
        ]
    elif mpc.pid == 2:
        secret_table = [
        [(3043159775188357783, 15235964463940002425, 9932488630110529569  ),(7232468392417487334, 10575557402460564869, 15273392327142801552  )],
        [(767062507945200306, 10327962038987350328, 7987850822477936301  ),(18267540472041889504, 11755363966658135568, 461719130564873112 )]
        ]

    secret_table = np.array(
        [[[secint(element) for element in sublist] for sublist in inner_list] for inner_list in secret_table]
    )

    #setting chain1
    my_aggregator_handler = AggregatorHandler()

    #request 
    input_request = {'secret_table': secret_table, 
                     'columnNo': 0, 
                     'aggregator': 'SUM'}
    result = await my_aggregator_handler.handle(input_request)
    logging.info('Result Chain1: {}'.format(result))


mpc.run(main())