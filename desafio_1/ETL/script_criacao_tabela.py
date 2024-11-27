import mysql.connector

# Conectando ao banco de dados no container MySQL
conn = mysql.connector.connect(
    host="localhost",          
    port=3306,                 
    user="admin",              
    password="1234",          
    database="coco_bambu"      
)

cursor = conn.cursor()

# Criação das tabelas

create_orders_table = """
CREATE TABLE IF NOT EXISTS Orders (
    guestCheckId BIGINT PRIMARY KEY,
    chkNum INT,
    opnUTC DATETIME,
    clsdUTC DATETIME,
    lastTransUTC DATETIME,
    lastUpdatedUTC DATETIME,
    gstCnt INT,
    subTtl DECIMAL(10, 2),
    payTtl DECIMAL(10, 2),
    balDueTtl DECIMAL(10, 2),
    rvcNum INT,
    otNum INT,
    tblNum INT,
    tblName VARCHAR(50),
    empNum INT,
    numSrvcRd INT,
    numChkPrntd INT,
    clsdFlag BOOLEAN
);
"""

create_orderitems_table = """
CREATE TABLE IF NOT EXISTS OrderItems (
    guestCheckLineItemId BIGINT PRIMARY KEY,
    guestCheckId BIGINT,
    menuItemId INT,
    quantity INT,
    price DECIMAL(10, 2),
    detailUTC DATETIME,
    lastUpdateUTC DATETIME,
    FOREIGN KEY (guestCheckId) REFERENCES Orders(guestCheckId)
);
"""

create_taxes_table = """
CREATE TABLE IF NOT EXISTS Taxes (
    taxNum INT PRIMARY KEY,
    guestCheckId BIGINT,
    txblSlsTtl DECIMAL(10, 2),
    taxCollTtl DECIMAL(10, 2),
    taxRate DECIMAL(5, 2),
    type INT,
    FOREIGN KEY (guestCheckId) REFERENCES Orders(guestCheckId)
);
"""

create_servicecharges_table = """
CREATE TABLE IF NOT EXISTS ServiceCharges (
    guestCheckLineItemId BIGINT,
    chargeAmount DECIMAL(10, 2),
    FOREIGN KEY (guestCheckLineItemId) REFERENCES OrderItems(guestCheckLineItemId)
);
"""



# Executando a criação das tabelas
try:
    cursor.execute(create_orders_table)
    cursor.execute(create_orderitems_table)
    cursor.execute(create_taxes_table)
    cursor.execute(create_servicecharges_table)
   
    
    print("Tabelas criadas com sucesso!")
except mysql.connector.Error as err:
    print(f"Erro ao criar as tabelas: {err}")
finally:
    cursor.close()
    conn.commit()  
    conn.close()   
