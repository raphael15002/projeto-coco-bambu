Análise do Esquema JSON - ERP.json



1. **Raiz do JSON**
   - **curUTC**: String (Data e hora no formato UTC)
   - **locRef**: String (Referência de local)
   - **guestChecks**: Lista de objetos (contém as informações do pedido)

2. **guestChecks** (Array de pedidos)
   - **guestCheckId**: Inteiro (Identificador único do pedido)
   - **chkNum**: Inteiro (Número do cheque)
   - **opnBusDt**: String (Data de abertura do pedido)
   - **opnUTC**: String (Hora de abertura no formato UTC)
   - **opnLcl**: String (Hora de abertura no formato local)
   - **clsdBusDt**: String (Data de fechamento do pedido)
   - **clsdUTC**: String (Hora de fechamento no formato UTC)
   - **clsdLcl**: String (Hora de fechamento no formato local)
   - **lastTransUTC**: String (Hora da última transação no formato UTC)
   - **lastTransLcl**: String (Hora da última transação no formato local)
   - **lastUpdatedUTC**: String (Hora da última atualização no formato UTC)
   - **lastUpdatedLcl**: String (Hora da última atualização no formato local)
   - **clsdFlag**: Boolean (Indica se o pedido está fechado)
   - **gstCnt**: Inteiro (Número de convidados)
   - **subTtl**: Decimal (Subtotal do pedido)
   - **nonTxblSlsTtl**: Decimal (Subtotal de vendas não tributáveis)
   - **chkTtl**: Decimal (Total do pedido)
   - **dscTtl**: Decimal (Desconto aplicado)
   - **payTtl**: Decimal (Total pago)
   - **balDueTtl**: Decimal (Saldo devido, se houver)
   - **rvcNum**: Inteiro (Número da receita)
   - **otNum**: Inteiro (Número da operação)
   - **ocNum**: Inteiro (Número do cliente, se houver)
   - **tblNum**: Inteiro (Número da mesa)
   - **tblName**: String (Nome da mesa)
   - **empNum**: Inteiro (Número do empregado que atendeu o pedido)
   - **numSrvcRd**: Inteiro (Número de serviços realizados)
   - **numChkPrntd**: Inteiro (Número de impressões do cheque)

3. **taxes** (Array de impostos)
   - **taxNum**: Inteiro (Número do imposto)
   - **txblSlsTtl**: Decimal (Total de vendas tributáveis)
   - **taxCollTtl**: Decimal (Total de imposto coletado)
   - **taxRate**: Decimal (Taxa de imposto)
   - **type**: Inteiro (Tipo de imposto)

4. **detailLines** (Array de itens do pedido)
   - **guestCheckLineItemId**: Inteiro (Identificador único do item no pedido)
   - **rvcNum**: Inteiro (Número da receita)
   - **dtlOtNum**: Inteiro (Número de operação do item)
   - **dtlOcNum**: Inteiro (Número do cliente do item)
   - **lineNum**: Inteiro (Número da linha do item no pedido)
   - **menuItem**: Objeto (Informações sobre o item de menu)

5. **menuItem** (Informações do item do cardápio)
   - **miNum**: Inteiro (Identificador do item no menu)
   - **modFlag**: Boolean (Indica se o item foi modificado)
   - **inclTax**: Decimal (Imposto incluído no preço do item)
   - **activeTaxes**: String (Impostos ativos associados ao item)
   - **prcLvl**: Inteiro (Nível de preço do item)