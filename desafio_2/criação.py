import os


data_lake_path = r"C:\Users\refol\OneDrive\Desktop\Projeto_coco_bambu\desafio_2"



store_ids = ['store_id_1', 'store_id_2']

# Criar a estrutura de pastas
for store_id in store_ids:
    store_path = os.path.join(data_lake_path, store_id)
    
    # Criar as pastas para cada loja
    os.makedirs(os.path.join(store_path, "fiscal_invoices", "2023"), exist_ok=True)
    os.makedirs(os.path.join(store_path, "guest_checks", "2023"), exist_ok=True)
    os.makedirs(os.path.join(store_path, "chargebacks", "2023"), exist_ok=True)
    os.makedirs(os.path.join(store_path, "transactions", "2023"), exist_ok=True)
    os.makedirs(os.path.join(store_path, "cash_management", "2023"), exist_ok=True)
    os.makedirs(os.path.join(store_path, "metadata"), exist_ok=True)

print("Estrutura de pastas criada com sucesso!")
