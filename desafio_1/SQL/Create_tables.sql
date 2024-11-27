
CREATE TABLE Orders (
    guestCheckId BIGINT PRIMARY KEY,          -- Identificador único do pedido
    chkNum INT,                               -- Número do cheque
    opnUTC DATETIME,                          -- Data e hora de abertura
    clsdUTC DATETIME,                         -- Data e hora de fechamento
    lastTransUTC DATETIME,                    -- Data e hora da última transação
    lastUpdatedUTC DATETIME,                  -- Data e hora da última atualização
    gstCnt INT,                               -- Número de convidados
    subTtl DECIMAL(10, 2),                    -- Subtotal do pedido
    payTtl DECIMAL(10, 2),                    -- Total pago
    balDueTtl DECIMAL(10, 2),                 -- Saldo devido (se houver)
    rvcNum INT,                               -- Número da receita
    otNum INT,                                -- Número da operação
    tblNum INT,                               -- Número da mesa
    tblName VARCHAR(50),                      -- Nome da mesa
    empNum INT,                               -- Número do empregado que atendeu o pedido
    numSrvcRd INT,                            -- Número de serviços realizados
    numChkPrntd INT,                          -- Número de impressões do cheque
    clsdFlag BOOLEAN                          -- Flag de fechado (True ou False)
);


CREATE TABLE OrderItems (
    guestCheckLineItemId BIGINT PRIMARY KEY,   -- Identificador único do item no pedido
    guestCheckId BIGINT,                       -- Relacionamento com o pedido (foreign key)
    menuItemId INT,                            -- Relacionamento com o item do menu
    quantity INT,                              -- Quantidade do item
    price DECIMAL(10, 2),                      -- Preço do item
    detailUTC DATETIME,                        -- Data e hora do detalhe do item
    lastUpdateUTC DATETIME,                    -- Última atualização
    FOREIGN KEY (guestCheckId) REFERENCES Orders(guestCheckId) -- Relacionamento com a tabela Orders
);


CREATE TABLE Taxes (
    taxNum INT PRIMARY KEY,                    -- Identificador da taxa
    guestCheckId BIGINT,                       -- Relacionamento com o pedido
    txblSlsTtl DECIMAL(10, 2),                 -- Total de vendas tributáveis
    taxCollTtl DECIMAL(10, 2),                 -- Total de imposto coletado
    taxRate DECIMAL(5, 2),                     -- Taxa de imposto
    type INT,                                  -- Tipo de taxa
    FOREIGN KEY (guestCheckId) REFERENCES Orders(guestCheckId) -- Relacionamento com a tabela Orders
);


CREATE TABLE ServiceCharges (
    guestCheckLineItemId BIGINT,               -- Relacionamento com o item do pedido
    chargeAmount DECIMAL(10, 2),               -- Valor da taxa de serviço
    FOREIGN KEY (guestCheckLineItemId) REFERENCES OrderItems(guestCheckLineItemId)
);

CREATE TABLE Payments (
    guestCheckLineItemId BIGINT,               -- Relacionamento com o item do pedido
    paymentMethod VARCHAR(50),                 -- Método de pagamento (Cartão de Crédito, Dinheiro, etc.)
    amount DECIMAL(10, 2),                     -- Valor pago
    FOREIGN KEY (guestCheckLineItemId) REFERENCES OrderItems(guestCheckLineItemId)
);


CREATE TABLE Errors (
    guestCheckLineItemId BIGINT,               -- Relacionamento com o item do pedido
    errorCode VARCHAR(50),                     -- Código do erro
    FOREIGN KEY (guestCheckLineItemId) REFERENCES OrderItems(guestCheckLineItemId)
);
