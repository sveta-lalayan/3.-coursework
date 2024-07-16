import json
from pprint import pprint

from config import PATH
from datetime import datetime


def load_data():
    '''Загружает json файл с данными EXECUTED'''
    with open(PATH, encoding='UTF-8') as read_data:
        data = json.load(read_data)
        operation_list = []
        for operation in data:
            if operation.get("state") == "EXECUTED":
                operation_list.append(operation)
        return operation_list


def five_items(sort_items):
    '''Отображает пять последних транзакций в списке'''
    sort_list = sorted(sort_items, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"),
                       reverse=True)
    last_five = sort_list[:5]
    return last_five


def correct_date(iso_date: str) -> str:
    dt = datetime.fromisoformat(iso_date)
    return dt.strftime('%d.%m.%Y')

# def correct_date(value):
#     '''Выыод даты в требуемом формате'''
#     date_list = []
#     for data in value:
#         date = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%f")
#         date_format = f'{date:%d.%m.%Y}'
#         date_list.append(date_format)
#     return date_list
# pprint(correct_date(load_data()))


def account_of_sender(account):
    '''Данные отправителя'''
    accountt = []
    accountt.append(account)
    for data in accountt:
        encrypted_account = []
        if data.get("from") is not None:
            account_list = data.get("from")
            encrypted_account.append(account_list[:-10] + '*' * 6 + account_list[-4:])
    return ''.join(encrypted_account)


def account_of_recipent(account):
    '''Данные получателя'''
    for data in account:
        encrypted_account = []
        if data.get("to") is not None:
            account_list = data.get("to")
            if "Счет" in account_list:
                encrypted_account.append(account_list[:-20] + '*' * 2 + account_list[-4:])
            else:
                encrypted_account.append(account_list[:-16] + '*' * 2 + account_list[-4:])

    return ''.join(encrypted_account)


def transfer_ammount(account):
    '''Сумма перевода'''
    transferr = []
    transferr.append(account)
    for data in transferr:
        transfer = []
        if data.get("state") == "EXECUTED":
            account_list = data["operationAmount"]["amount"]
            transfer.append(account_list)
    return ''.join(transfer)

def currency(account):
    '''Валюта перевода'''
    transferr = []
    transferr.append(account)
    for data in transferr:
        transfer = []
        if data.get("state") == "EXECUTED":
            account_list = data["operationAmount"]["currency"]["name"]
            transfer.append(account_list)
    return ''.join(transfer)




