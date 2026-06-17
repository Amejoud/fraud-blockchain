import sys
import os

# Permet d'importer les autres fichiers du dossier 'src'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_loader import load_data
from fraud_detector import detect_fraud
from blockchain import Blockchain

def main():
    print("="*40)
    print("🚀 SYSTÈME DE DÉTECTION DE FRAUDE")
    print("="*40)

    # 1. Charger les données
    df = load_data()
    print(f"✅ {len(df)} transactions chargées.\n")

    # 2. Détecter les fraudes
    frauds = detect_fraud(df)
    print(f"️  {len(frauds)} transactions suspectes trouvées !\n")

    # 3. Enregistrer dans la Blockchain
    print("Création de la Blockchain...")
    bc = Blockchain()
    
    for index, row in frauds.iterrows():
        bc.add_transaction(row.to_dict())
        
    new_block = bc.mine_block()
    
    if new_block:
        print(f"✅ Bloc miné avec succès !")
        print(f"🔗 Hash du bloc : {new_block.hash[:20]}...")
        print(f"🔒 Hash du bloc précédent : {new_block.previous_hash[:20]}...\n")

    # 4. Vérifier l'intégrité
    is_valid = bc.is_valid()
    print(f"️ La Blockchain est-elle valide et intacte ? {'OUI ✅' if is_valid else 'NON '}")
    print("="*40)

if __name__ == "__main__":
    main()