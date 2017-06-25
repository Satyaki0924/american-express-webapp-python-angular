import os

import pandas as pd


class Collect:
    @staticmethod
    def pass_dataframe():
        df = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + '/userdb/credit_card57066ea.csv')
        df['SEX'] = df['SEX'].map({1: 'Male', 2: 'Female'})
        df['default.payment.next.month'] = df['default.payment.next.month'].map({1: 'Yes', 0: 'No'})
        df['EDUCATION'] = df['EDUCATION'].map(
            {1: 'Graduate school', 2: 'University', 3: 'High school', 4: 'Others', 5: 'Unknown', 6: 'Unknown'})
        df['MARRIAGE'] = df['MARRIAGE'].map({1: 'Married', 2: 'Single', 4: 'Others'})
        df['PAY_0'] = df['PAY_0'].map(
            {-2: 'No bill amount for the month', -1: 'Pay duly', 1: 'Payment delay for one month'
                , 2: 'Payment delay for two months'
                , 3: 'Payment delay for three months'
                , 4: 'Payment delay for four months'
                , 5: 'Payment delay for five months',
             6: 'Payment delay for six months',
             7: 'Payment delay for seven months',
             8: 'payment delay for eight months',
             9: 'payment delay for nine months and above'})
        df['PAY_2'] = df['PAY_2'].map(
            {-2: 'No bill amount for the month', -1: 'Pay duly', 1: 'Payment delay for one month'
                , 2: 'Payment delay for two months'
                , 3: 'Payment delay for three months'
                , 4: 'Payment delay for four months'
                , 5: 'Payment delay for five months',
             6: 'Payment delay for six months',
             7: 'Payment delay for seven months',
             8: 'payment delay for eight months',
             9: 'payment delay for nine months and above'})
        df['PAY_3'] = df['PAY_3'].map(
            {-2: 'No bill amount for the month', -1: 'Pay duly', 1: 'Payment delay for one month'
                , 2: 'Payment delay for two months'
                , 3: 'Payment delay for three months'
                , 4: 'Payment delay for four months'
                , 5: 'Payment delay for five months',
             6: 'Payment delay for six months',
             7: 'Payment delay for seven months',
             8: 'payment delay for eight months',
             9: 'payment delay for nine months and above'})
        df['PAY_4'] = df['PAY_4'].map(
            {-2: 'No bill amount for the month', -1: 'Pay duly', 1: 'Payment delay for one month'
                , 2: 'Payment delay for two months'
                , 3: 'Payment delay for three months'
                , 4: 'Payment delay for four months'
                , 5: 'Payment delay for five months',
             6: 'Payment delay for six months',
             7: 'Payment delay for seven months',
             8: 'payment delay for eight months',
             9: 'payment delay for nine months and above'})
        df['PAY_5'] = df['PAY_5'].map(
            {-2: 'No bill amount for the month', -1: 'Pay duly', 1: 'Payment delay for one month'
                , 2: 'Payment delay for two months'
                , 3: 'Payment delay for three months'
                , 4: 'Payment delay for four months'
                , 5: 'Payment delay for five months',
             6: 'Payment delay for six months',
             7: 'Payment delay for seven months',
             8: 'payment delay for eight months',
             9: 'payment delay for nine months and above'})

        return df

    @staticmethod
    def collect_payment(id):
        df = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + '/userdb/credit_card57066ea.csv')

        return df['Name'][id], [
            df['BILL_AMT6'][id], df['BILL_AMT5'][id], df['BILL_AMT4'][id], df['BILL_AMT3'][id], df['BILL_AMT2'][id],
            df['BILL_AMT1'][id]]

    @staticmethod
    def collect_payment2(id):
        df = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + '/userdb/credit_card57066ea.csv')

        return df['Name'][id], [
            df['PAY_AMT6'][id], df['PAY_AMT5'][id], df['PAY_AMT4'][id], df['PAY_AMT3'][id], df['PAY_AMT2'][id],
            df['PAY_AMT1'][id]]


