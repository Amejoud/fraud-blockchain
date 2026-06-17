import customtkinter as ctk
from tkinter import ttk, messagebox
import sys
import os

# Ajouter le dossier src au path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data_loader import load_data
from src.fraud_detector import detect_fraud
from src.blockchain import Blockchain

# Configuration du thème
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FraudDetectionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.title("Systeme de Detection de Fraude avec Blockchain")
        self.geometry("1200x700")
        self.minsize(1000, 600)
        
        # Variables
        self.data = None
        self.frauds = None
        self.blockchain = None
        
        # Créer l'interface
        self.create_widgets()
        
    def create_widgets(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self, fg_color="#1a1a2e")
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Titre
        title_label = ctk.CTkLabel(
            main_frame,
            text="SYSTEME DE DETECTION DE FRAUDE AVEC BLOCKCHAIN",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#00d9ff"
        )
        title_label.pack(pady=20)
        
        # Frame pour les boutons
        btn_frame = ctk.CTkFrame(main_frame, fg_color="#16213e")
        btn_frame.pack(fill="x", padx=20, pady=15)
        
        self.btn_load = ctk.CTkButton(
            btn_frame,
            text="CHARGER LES DONNEES",
            command=self.load_data,
            height=45,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#0f3460",
            hover_color="#1a5f7a",
            text_color="white"
        )
        self.btn_load.pack(side="left", padx=15, pady=15)
        
        self.btn_detect = ctk.CTkButton(
            btn_frame,
            text="DETECTER LES FRAUDES",
            command=self.detect_fraud_ui,
            height=45,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#e94560",
            hover_color="#c73e54",
            text_color="white",
            state="disabled"
        )
        self.btn_detect.pack(side="left", padx=15, pady=15)
        
        self.btn_blockchain = ctk.CTkButton(
            btn_frame,
            text="CREER BLOCKCHAIN",
            command=self.create_blockchain_ui,
            height=45,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#533483",
            hover_color="#3d2463",
            text_color="white",
            state="disabled"
        )
        self.btn_blockchain.pack(side="left", padx=15, pady=15)
        
        # Frame pour les statistiques
        stats_frame = ctk.CTkFrame(main_frame, fg_color="#16213e")
        stats_frame.pack(fill="x", padx=20, pady=15)
        
        self.stats_labels = {}
        stats_config = [
            ("Total Transactions", "0", "#0f3460"),
            ("Montant Total", "$0", "#00d9ff"),
            ("Transactions Normales", "0", "#00b894"),
            ("Transactions Suspectes", "0", "#e94560")
        ]
        
        for i, (title, value, color) in enumerate(stats_config):
            frame = ctk.CTkFrame(stats_frame, fg_color=color)
            frame.grid(row=0, column=i, padx=10, pady=10, sticky="ew")
            stats_frame.grid_columnconfigure(i, weight=1)
            
            label_title = ctk.CTkLabel(
                frame, 
                text=title, 
                font=ctk.CTkFont(size=11),
                text_color="white"
            )
            label_title.pack(pady=(10, 5))
            
            label_value = ctk.CTkLabel(
                frame, 
                text=value, 
                font=ctk.CTkFont(size=22, weight="bold"),
                text_color="white"
            )
            label_value.pack(pady=(0, 10))
            
            self.stats_labels[title] = label_value
        
        # Frame pour le tableau
        table_frame = ctk.CTkFrame(main_frame, fg_color="#16213e")
        table_frame.pack(fill="both", expand=True, padx=20, pady=15)
        
        # Titre du tableau
        table_title = ctk.CTkLabel(
            table_frame,
            text="DONNEES DES TRANSACTIONS",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#00d9ff"
        )
        table_title.pack(pady=10)
        
        # Créer le tableau avec ttk
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                       background="#0f3460",
                       foreground="white",
                       fieldbackground="#0f3460",
                       rowheight=30,
                       font=("Arial", 10),
                       bordercolor="#16213e",
                       lightcolor="#16213e",
                       darkcolor="#16213e")
        style.configure("Treeview.Heading",
                       background="#1a1a2e",
                       foreground="#00d9ff",
                       font=("Arial", 11, "bold"),
                       relief="flat")
        style.map("Treeview",
                 background=[('selected', '#e94560')],
                 foreground=[('selected', 'white')])
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.tree = ttk.Treeview(
            table_frame,
            columns=("id", "sender", "receiver", "amount", "status"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        
        self.tree.heading("id", text="ID")
        self.tree.heading("sender", text="EXPEDITEUR")
        self.tree.heading("receiver", text="DESTINATAIRE")
        self.tree.heading("amount", text="MONTANT ($)")
        self.tree.heading("status", text="STATUT")
        
        self.tree.column("id", width=60, anchor="center")
        self.tree.column("sender", width=150, anchor="center")
        self.tree.column("receiver", width=150, anchor="center")
        self.tree.column("amount", width=120, anchor="center")
        self.tree.column("status", width=180, anchor="center")
        
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar.config(command=self.tree.yview)
        
        # Frame pour les infos blockchain
        self.blockchain_frame = ctk.CTkFrame(main_frame, fg_color="#16213e")
        self.blockchain_frame.pack(fill="x", padx=20, pady=15)
        
        blockchain_title = ctk.CTkLabel(
            self.blockchain_frame,
            text="INFORMATIONS BLOCKCHAIN",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#533483"
        )
        blockchain_title.pack(pady=10)
        
        self.blockchain_info = ctk.CTkLabel(
            self.blockchain_frame,
            text="En attente de creation...",
            font=ctk.CTkFont(size=11),
            text_color="#7f8c8d",
            justify="left"
        )
        self.blockchain_info.pack(pady=10)
        
        # Barre de statut
        self.status_bar = ctk.CTkLabel(
            main_frame,
            text="Pret",
            font=ctk.CTkFont(size=12),
            text_color="#00b894",
            fg_color="#16213e"
        )
        self.status_bar.pack(pady=10, padx=20, fill="x")
        
    def load_data(self):
        try:
            self.status_bar.configure(text="Chargement des donnees...", text_color="#f39c12")
            self.update()
            
            self.data = load_data()
            
            # Mettre à jour les statistiques
            total = len(self.data)
            total_amount = self.data['amount'].sum()
            
            self.stats_labels["Total Transactions"].configure(text=str(total))
            self.stats_labels["Montant Total"].configure(text=f"${total_amount:,}")
            
            # Remplir le tableau
            for row in self.tree.get_children():
                self.tree.delete(row)
            
            for _, row in self.data.iterrows():
                self.tree.insert("", "end", values=(
                    row['id'],
                    row['sender'],
                    row['receiver'],
                    f"${row['amount']}",
                    "En attente"
                ))
            
            self.btn_load.configure(state="normal")
            self.btn_detect.configure(state="normal")
            self.status_bar.configure(text=f"{total} transactions chargees avec succes!", text_color="#00b894")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement: {e}")
            self.status_bar.configure(text="Erreur de chargement", text_color="#e94560")
            
    def detect_fraud_ui(self):
        if self.data is None:
            messagebox.showwarning("Attention", "Veuillez d'abord charger les donnees")
            return
            
        try:
            self.status_bar.configure(text="Analyse en cours...", text_color="#f39c12")
            self.update()
            
            self.frauds = detect_fraud(self.data)
            
            # Mettre à jour les statistiques
            normal_count = len(self.data) - len(self.frauds)
            fraud_count = len(self.frauds)
            
            self.stats_labels["Transactions Normales"].configure(text=str(normal_count))
            self.stats_labels["Transactions Suspectes"].configure(text=str(fraud_count))
            
            # Mettre à jour le tableau
            for row in self.tree.get_children():
                self.tree.delete(row)
            
            for _, row in self.data.iterrows():
                status = "SUSPECTE" if row['id'] in self.frauds['id'].values else "Normale"
                self.tree.insert("", "end", values=(
                    row['id'],
                    row['sender'],
                    row['receiver'],
                    f"${row['amount']}",
                    status
                ))
            
            self.btn_blockchain.configure(state="normal")
            self.status_bar.configure(text=f"Analyse terminee! {fraud_count} fraudes detectees", text_color="#00b894")
            
            if fraud_count > 0:
                messagebox.showinfo("Resultat", f"{fraud_count} transactions suspectes detectees!")
                
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'analyse: {e}")
            self.status_bar.configure(text="Erreur d'analyse", text_color="#e94560")
            
    def create_blockchain_ui(self):
        if self.frauds is None or len(self.frauds) == 0:
            messagebox.showwarning("Attention", "Aucune fraude a enregistrer")
            return
            
        try:
            self.status_bar.configure(text="Creation de la blockchain...", text_color="#f39c12")
            self.update()
            
            self.blockchain = Blockchain()
            
            for index, row in self.frauds.iterrows():
                self.blockchain.add_transaction(row.to_dict())
            
            new_block = self.blockchain.mine_block()
            
            if new_block:
                is_valid = self.blockchain.is_valid()
                
                info_text = f"""
                Blockchain creee avec succes!
                
                Nombre de blocs: {len(self.blockchain.chain)}
                Hash du bloc: {new_block.hash[:35]}...
                Hash precedent: {new_block.previous_hash[:35]}...
                Timestamp: {new_block.timestamp}
                Validation: {'VALIDE' if is_valid else 'INVALIDE'}
                """
                
                self.blockchain_info.configure(
                    text=info_text, 
                    text_color="#00b894",
                    font=ctk.CTkFont(size=10)
                )
                self.status_bar.configure(text="Blockchain creee et validee!", text_color="#00b894")
                messagebox.showinfo("Succes", "Blockchain creee avec succes!")
                
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la creation: {e}")
            self.status_bar.configure(text="Erreur de creation", text_color="#e94560")

if __name__ == "__main__":
    app = FraudDetectionApp()
    app.mainloop()