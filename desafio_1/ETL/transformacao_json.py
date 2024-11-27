import os
import json
import pymysql
from datetime import datetime


def connect_to_db():
    return pymysql.connect(
    host="localhost",          
    port=3306,                 
    user="admin",              
    password="1234",          
    database="coco_bambu"  
    )


def check_file_exists(file_path):
    if not os.path.exists(file_path):
        print(f"Erro: O arquivo {file_path} não foi encontrado!")
        return False
    return True


def convert_to_datetime(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return None  


def insert_data_from_json(json_file):
    if not check_file_exists(json_file):
        return  


    conn = connect_to_db()
    cursor = conn.cursor()

  
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for guest_check in data['guestChecks']:
        opnUTC = convert_to_datetime(guest_check['opnUTC'])
        clsdUTC = convert_to_datetime(guest_check['clsdUTC'])
        lastTransUTC = convert_to_datetime(guest_check['lastTransUTC'])
        lastUpdatedUTC = convert_to_datetime(guest_check['lastUpdatedUTC'])

        cursor.execute(''' 
            INSERT INTO Orders (guestCheckId, opnUTC, clsdUTC, lastTransUTC, lastUpdatedUTC, 
                                chkNum, gstCnt, subTtl, payTtl, rvcNum, otNum, tblNum, tblName, empNum, numSrvcRd, numChkPrntd, clsdFlag)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            guest_check['guestCheckId'],
            opnUTC,
            clsdUTC,
            lastTransUTC,
            lastUpdatedUTC,
            guest_check['chkNum'],
            guest_check['gstCnt'],
            guest_check['subTtl'],
            guest_check['payTtl'],
            guest_check['rvcNum'],
            guest_check['otNum'],
            guest_check['tblNum'],
            guest_check['tblName'],
            guest_check['empNum'],
            guest_check['numSrvcRd'],
            guest_check['numChkPrntd'],
            guest_check['clsdFlag']
        ))

        # Inserir os dados na tabela OrderItems
        for detail in guest_check['detailLines']:
            detailUTC = convert_to_datetime(detail['detailUTC'])
            lastUpdateUTC = convert_to_datetime(detail['lastUpdateUTC'])
            menu_item_id = detail['menuItem']['miNum']  # Usando 'miNum' como 'menuItemId'
            quantity = detail['dspQty']  # Usando 'dspQty' como quantidade
            price = detail['dspTtl']  # Usando 'dspTtl' como preço

            cursor.execute('''
                INSERT INTO OrderItems (guestCheckLineItemId, guestCheckId, menuItemId, quantity, price, detailUTC, lastUpdateUTC)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (
                detail['guestCheckLineItemId'],
                guest_check['guestCheckId'],
                menu_item_id,
                quantity,
                price,
                detailUTC,
                lastUpdateUTC
            ))

        # Inserir os dados na tabela Taxes (taxes)
        for tax in guest_check['taxes']:
            cursor.execute('''
                INSERT INTO Taxes (guestCheckId, taxNum, txblSlsTtl, taxCollTtl, taxRate, type)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (
                guest_check['guestCheckId'],
                tax['taxNum'],
                tax['txblSlsTtl'],
                tax['taxCollTtl'],
                tax['taxRate'],
                tax['type']
            ))

        # Inserir os dados na tabela ServiceCharges (service charges)
        for detail in guest_check['detailLines']:
            if 'svcRndNum' in detail:  # Verifica se existe a chave 'svcRndNum'
                cursor.execute('''
                    INSERT INTO ServiceCharges (guestCheckLineItemId, chargeAmount)
                    VALUES (%s, %s)
                ''', (
                    detail['guestCheckLineItemId'],
                    detail.get('svcRndNum', 0)  # Usando 0 se a chave não existir
                ))

        # Inserir os dados na tabela Payments (payments)
        for detail in guest_check['detailLines']:
            if 'paymentMethod' in detail:  # Verifica se existe a chave 'paymentMethod'
                cursor.execute('''
                    INSERT INTO Payments (guestCheckLineItemId, paymentMethod, amount)
                    VALUES (%s, %s, %s)
                ''', (
                    detail['guestCheckLineItemId'],
                    detail['paymentMethod'],
                    detail.get('amount', 0)  # Usando 0 se a chave não existir
                ))

        # Inserir os dados na tabela Errors (errors)
        for detail in guest_check['detailLines']:
            if 'errorCode' in detail:  # Verifica se existe a chave 'errorCode'
                cursor.execute('''
                    INSERT INTO Errors (guestCheckLineItemId, errorCode)
                    VALUES (%s, %s)
                ''', (
                    detail['guestCheckLineItemId'],
                    detail['errorCode']
                ))

        
        conn.commit()

  
    cursor.close()
    conn.close()



file_path = "C:\\Users\\refol\\OneDrive\\Desktop\\projeto-coco-bambu\\desafio_1\\ETL\\ERP.json"




insert_data_from_json(file_path)
