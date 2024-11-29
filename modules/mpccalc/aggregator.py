from modules.mpccalc.handlerabstract import AbstractHandler
from typing import Dict
from mpyc.runtime import mpc
import numpy as np
import logging

class AggregatorHandler(AbstractHandler):
    async def handle(self, request: Dict) -> int:
        secret_table = request['secret_table']
        columnNo = request['columnNo']
        aggregator = request['aggregator']
        condList = request.get('condList', None)
        aggregatorDict = {
            'SUM': self.aggregate_sum,
            'COUNT': self.aggregate_count
        }

        if aggregator in aggregatorDict:
            return await aggregatorDict[aggregator](secret_table, columnNo, condList)
        else:
            return None

    async def aggregate_sum(self, secret_table, columnNo, condList):
            logging.info("Aggregator: I'll aggregate the SUM")
            newList = []
            columnItemSum = 0
            my_column = secret_table[:,columnNo]
            if condList:
                for index, cond in zip(np.ndindex(my_column.shape), condList):
                    x = mpc.if_else(cond, 0, my_column[index])
                    newList.append(x)
            else:
                for index in np.ndindex(my_column.shape):
                    newList.append(my_column[index])
            columnItemSum = mpc.sum(newList)
            total = await mpc.output(columnItemSum)
            logging.info('Total Colum1: {}'.format(total))
            logging.info('super: {}'.format( super()._next_handler))
            if super()._next_handler:
                return await super().handle(total)
            else:
                return total
        
    async def aggregate_count(self, secret_table, columnNo, condList):
            logging.info("Aggregator: I'll aggregate the COUNT")
            newList = []
            my_column = secret_table[:,columnNo]
            #count = len([my_column[index] for index in np.ndindex(my_column.shape) if not isinstance(my_column[index], int)])
            if condList:
                 for index, cond in zip(np.ndindex(my_column.shape), condList):
                     x = mpc.if_else(cond, 0, my_column[index])
                     newList.append(x)
            else:
                for index in np.ndindex(my_column.shape):
                    newList.append(my_column[index])
            count = len(newList)
            logging.info('Count Colum1: {}'.format(count))
            if super()._next_handler:
                 return await super().handle(count)
            else:
                return count