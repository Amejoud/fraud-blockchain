import customtkinter as ctk
from tkinter import ttk, messagebox, filedialog
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data_loader import load_data
from src.fraud_detector import detect_fraud
from src.blockchain import Blockchain

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FraudDetectionDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard - Detection de Fraude Blockchain")
        self.geometry("1400x800")
        self.minsize(1200, 700)
        self.data = None
        self.frauds = None
        self.blockchain = None
        self.create_dashboard()
        
    def create_dashboard(self):
        main_container = ctk.CTkFrame(self, fg_color="#0a0e27")
        main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        header = ctk.CTkFrame(main_container, fg_color="#1a1f4d", height=80)
        header.pack(fill="x", pady=(0, 10))
        header.pack_propagate(False)
        
        ctk.CTkLabel(
            header,
            text="DASHBOARD - DETECTION DE FRAUDE AVEC BLOCKCHAIN",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#00d9ff"
        ).pack(pady=25)
        
        sidebar = ctk.CTkFrame(main_container, fg_color="#161b3d", width=200)
        sidebar.pack(side="left", fill="y", padx=(0, 10))
        sidebar.pack_propagate(False)
        
        ctk.CTkButton(
            sidebar, text="Tableau de Bord", 
            command=self.show_dashboard_view,
            fg_color="#0f3460", hover_color="#1a5f7a",
            font=ctk.CTkFont(size=12), height=40, anchor="w"
        ).pack(fill="x", pady=5, padx=10)
        
        ctk.CTkButton(
            sidebar, text="Donnees",
            command=self.show_data_view,
            fg_color="#0f3460", hover_color="#1a5f7a",
            font=ctk.CTkFont(size=12), height=40, anchor="w"
        ).pack(fill="x", pady=5, padx=10)
        
        ctk.CTkButton(
            sidebar, text="Statistiques",
            command=self.show_analytics_view,
            fg_color="#0f3460", hover_color="#1a5f7a",
            font=ctk.CTkFont(size=12), height=40, anchor="w"
        ).pack(fill="x", pady=5, padx=10)
        
        ctk.CTkButton(
            sidebar, text="Blockchain",
            command=self.show_blockchain_view,
            fg_color="#0f3460", hover_color="#1a5f7a",
            font=ctk.CTkFont(size=12), height=40, anchor="w"
        ).pack(fill="x", pady=5, padx=10)
        
        ctk.CTkLabel(sidebar, text="", height=20).pack()
        
        ctk.CTkButton(
            sidebar, text="Exporter",
            command=self.export_data,
            fg_color="#e94560", hover_color="#c73e54",
            font=ctk.CTkFont(size=12), height=40, anchor="w"
        ).pack(fill="x", pady=5, padx=10)
        
        self.content_frame = ctk.CTkFrame(main_container, fg_color="#1a1f4d")
        self.content_frame.pack(side="left", fill="both", expand=True)
        
        self.show_dashboard_view()
        
    def show_dashboard_view(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        stats_frame = ctk.CTkFrame(self.content_frame, fg_color="#161b3d")
        stats_frame.pack(fill="x", padx=15, pady=15)
        
        if self.data is not None:
            total = len(self.data)
            total_amount = self.data['amount'].sum()
            avg_amount = self.data['amount'].mean()
            max_amount = self.data['amount'].max()
            fraud_count = len(self.frauds) if self.frauds is not None else 0
            
            stats = [
                ("Total Transactions", str(total), "#0f3460"),
                ("Montant Total", f"${total_amount:,.0f}", "#00d9ff"),
                ("Montant Moyen", f"${avg_amount:,.2f}", "#00b894"),
                ("Max Transaction", f"${max_amount:,.0f}", "#fdcb6e"),
                ("Fraudes Detectees", str(fraud_count), "#e94560"),
            ]
            
            for i, (title, value, color) in enumerate(stats):
                frame = ctk.CTkFrame(stats_frame, fg_color=color)
                frame.grid(row=0, column=i, padx=8, pady=10, sticky="ew")
                stats_frame.grid_columnconfigure(i, weight=1)
                ctk.CTkLabel(frame, text=title, font=ctk.CTkFont(size=10), text_color="white").pack(pady=(8, 2))
                ctk.CTkLabel(frame, text=value, font=ctk.CTkFont(size=18, weight="bold"), text_color="white").pack(pady=(0, 8))
        else:
            ctk.CTkLabel(stats_frame, text="Chargez les donnees pour voir les statistiques",
                        font=ctk.CTkFont(size=14), text_color="#7f8c8d").pack(pady=20)
        
        action_frame = ctk.CTkFrame(self.content_frame, fg_color="#161b3d")
        action_frame.pack(fill="x", padx=15, pady=15)
        
        ctk.CTkButton(action_frame, text="Charger Donnees", command=self.load_data,
                     fg_color="#0f3460", hover_color="#1a5f7a", height=35).pack(side="left", padx=5)
        
        ctk.CTkButton(action_frame, text="Detecter Fraudes", command=self.detect_fraud_ui,
                     fg_color="#e94560", hover_color="#c73e54", height=35).pack(side="left", padx=5)
        
        ctk.CTkButton(action_frame, text="Creer Blockchain", command=self.create_blockchain_ui,
                     fg_color="#533483", hover_color="#3d2463", height=35).pack(side="left", padx=5)
        
        ctk.CTkLabel(self.content_frame, text="Cliquez sur 'Statistiques' pour voir les graphiques",
                    font=ctk.CTkFont(size=14), text_color="#7f8c8d").pack(pady=50)
        
    def show_data_view(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        ctk.CTkLabel(self.content_frame, text="DONNEES DES TRANSACTIONS",
                    font=ctk.CTkFont(size=18, weight="bold"), text_color="#00d9ff").pack(pady=15)
        
        if self.data is not None:
            table_frame = ctk.CTkFrame(self.content_frame, fg_color="#161b3d")
            table_frame.pack(fill="both", expand=True, padx=15, pady=15)
            
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview", background="#0f3460", foreground="white",
                          fieldbackground="#0f3460", rowheight=28, font=("Arial", 10))
            style.configure("Treeview.Heading", background="#1a1f4d", foreground="#00d9ff",
                          font=("Arial", 11, "bold"))
            
            scrollbar = ttk.Scrollbar(table_frame)
            scrollbar.pack(side="right", fill="y")
            
            tree = ttk.Treeview(table_frame, columns=("id", "sender", "receiver", "amount"),
                              show="headings", yscrollcommand=scrollbar.set)
            
            for col, heading in [("id", "ID"), ("sender", "Expediteur"),
                               ("receiver", "Destinataire"), ("amount", "Montant ($)")]:
                tree.heading(col, text=heading)
                tree.column(col, width=150, anchor="center")
            
            for _, row in self.data.iterrows():
                tree.insert("", "end", values=(row['id'], row['sender'], row['receiver'], f"${row['amount']}"))
            
            tree.pack(fill="both", expand=True, padx=10, pady=10)
            scrollbar.config(command=tree.yview)
        else:
            ctk.CTkLabel(self.content_frame, text="Aucune donnee chargee",
                        font=ctk.CTkFont(size=14), text_color="#7f8c8d").pack(pady=50)
    
    def show_analytics_view(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        ctk.CTkLabel(self.content_frame, text="ANALYTIQUES ET STATISTIQUES",
                    font=ctk.CTkFont(size=18, weight="bold"), text_color="#00d9ff").pack(pady=15)
        
        if self.data is not None:
            fig, axes = plt.subplots(2, 2, figsize=(10, 8))
            fig.patch.set_facecolor('#161b3d')
            
            axes[0, 0].hist(self.data['amount'], bins=10, color='#00d9ff', edgecolor='white', alpha=0.7)
            axes[0, 0].set_title('Distribution des Montants', color='white', fontsize=10)
            axes[0, 0].set_facecolor('#0f3460')
            axes[0, 0].tick_params(colors='white')
            
            top_10 = self.data.nlargest(10, 'amount')
            axes[0, 1].barh(range(len(top_10)), top_10['amount'], color='#e94560', alpha=0.7)
            axes[0, 1].set_title('Top 10 Transactions', color='white', fontsize=10)
            axes[0, 1].set_facecolor('#0f3460')
            axes[0, 1].tick_params(colors='white')
            axes[0, 1].set_yticks(range(len(top_10)))
            axes[0, 1].set_yticklabels([f"ID {int(i)}" for i in top_10['id']], fontsize=8)
            
            stats = [self.data['amount'].sum(), self.data['amount'].mean(), 
                    self.data['amount'].max(), self.data['amount'].min()]
            labels = ['Total', 'Moyenne', 'Max', 'Min']
            colors = ['#00b894', '#fdcb6e', '#e94560', '#00d9ff']
            axes[1, 0].pie(stats, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
            axes[1, 0].set_title('Repartition Statistique', color='white', fontsize=10)
            
            axes[1, 1].scatter(self.data['id'], self.data['amount'], c='#00d9ff', alpha=0.6, s=50)
            axes[1, 1].axhline(y=1000, color='#e94560', linestyle='--', label='Seuil fraude (1000)')
            axes[1, 1].set_title('Transactions vs ID', color='white', fontsize=10)
            axes[1, 1].set_facecolor('#0f3460')
            axes[1, 1].tick_params(colors='white')
            axes[1, 1].legend(facecolor='#0f3460', labelcolor='white')
            
            plt.tight_layout()
            
            canvas_frame = ctk.CTkFrame(self.content_frame, fg_color="#161b3d")
            canvas_frame.pack(fill="both", expand=True, padx=15, pady=15)
            
            canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)
        else:
            ctk.CTkLabel(self.content_frame, text="Chargez les donnees pour voir les graphiques",
                        font=ctk.CTkFont(size=14), text_color="#7f8c8d").pack(pady=50)
    
    def show_blockchain_view(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        ctk.CTkLabel(self.content_frame, text="INFORMATIONS BLOCKCHAIN",
                    font=ctk.CTkFont(size=18, weight="bold"), text_color="#533483").pack(pady=15)
        
        if self.blockchain is not None:
            info_text = (f"Nombre de blocs: {len(self.blockchain.chain)}\n"
                        f"Transactions en attente: {len(self.blockchain.pending_transactions)}\n\n"
                        f"Dernier bloc:\n"
                        f"- Index: {self.blockchain.chain[-1].index}\n"
                        f"- Hash: {self.blockchain.chain[-1].hash[:50]}...\n"
                        f"- Timestamp: {self.blockchain.chain[-1].timestamp}\n"
                        f"- Transactions: {len(self.blockchain.chain[-1].transactions)}\n\n"
                        f"Validation: {'VALIDE' if self.blockchain.is_valid() else 'INVALIDE'}")
            
            ctk.CTkLabel(self.content_frame, text=info_text,
                        font=ctk.CTkFont(size=11), text_color="#00b894", justify="left").pack(pady=20, padx=20, fill="x")
        else:
            ctk.CTkLabel(self.content_frame, text="Blockchain non creee",
                        font=ctk.CTkFont(size=14), text_color="#7f8c8d").pack(pady=50)
    
    def load_data(self):
        try:
            self.data = load_data()
            messagebox.showinfo("Succes", f"{len(self.data)} transactions chargees!")
            self.show_dashboard_view()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur de chargement: {e}")
    
    def detect_fraud_ui(self):
        if self.data is None:
            messagebox.showwarning("Attention", "Chargez d'abord les donnees")
            return
        self.frauds = detect_fraud(self.data)
        messagebox.showinfo("Resultat", f"{len(self.frauds)} fraudes detectees!")
        self.show_dashboard_view()
    
    def create_blockchain_ui(self):
        if self.frauds is None or len(self.frauds) == 0:
            messagebox.showwarning("Attention", "Aucune fraude a enregistrer")
            return
        self.blockchain = Blockchain()
        for _, row in self.frauds.iterrows():
            self.blockchain.add_transaction(row.to_dict())
        self.blockchain.mine_block()
        messagebox.showinfo("Succes", "Blockchain creee avec succes!")
        self.show_blockchain_view()
    
    def export_data(self):
        if self.data is None:
            messagebox.showwarning("Attention", "Aucune donnee a exporter")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    self.data.to_csv(file_path, index=False)
                else:
                    self.data.to_excel(file_path, index=False)
                messagebox.showinfo("Succes", "Donnees exportees avec succes!")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur d'export: {e}")

if __name__ == "__main__":
    app = FraudDetectionDashboard()
    app.mainloop()