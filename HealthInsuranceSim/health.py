
import math

import math


class HealthInsurance:
    def __init__(self, comp_name):
        self.__name = comp_name
        self.__plans = {}

    def policy_names(self):
        names = []
        for name in self.__plans.keys():
            names.append(name)
        return names

    def policy_info(self, name):
        if self.__check(name):
            return self.__plans[name]
        else:
            return None

    def get_data(self):
        return self.__plans

    def get_deduc(self):
        deductibles = []
        for info in self.__plans.values():
            if info[0] not in deductibles:
                deductibles.append(info[0])
        return deductibles

    def get_coin(self):
        coinsurances = []
        for info in self.__plans.values():
            if info[1] not in coinsurances:
                coinsurances.append(info[1])
        return coinsurances

    def get_stlo(self):
        stoplosses = []
        for info in self.__plans.values():
            if info[2] not in stoplosses:
                stoplosses.append(info[2])
        return stoplosses

    def __check(self, name):
        return name in self.__plans

    def add_policy(self, name, deductible, coinsurance, stoploss):
        if not self.__check(name):
            self.__plans[name] = [deductible, coinsurance, stoploss]
        return self.__plans

    def pocket_cost(self, name):
        if self.__check(name):
            deductible, coinsurance, stoploss = self.__plans[name]
            cost = deductible + ((coinsurance * stoploss) / 100)
            return 'For ' + name + ' plan, the out-of-pocket maximum is $' + str(math.floor(cost))

    def __str__(self):
        num_plans = len(self.__plans)
        return 'The ' + self.__name.lower() + ' health insurance company offers ' + str(num_plans) + ' policies'