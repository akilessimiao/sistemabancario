import tkinter as tk
from tkinter import messagebox

class BancoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Agência Bancária")

        # Criando os widgets
        self.label_usuario = tk.Label(root, text="Usuário:")
        self.label_senha = tk.Label(root, text="Senha:")
        self.entry_usuario = tk.Entry(root)
        self.entry_senha = tk.Entry(root, show="*")
        self.button_login = tk.Button(root, text="Login", command=self.login)

        # Posicionando os widgets na tela
        self.label_usuario.grid(row=0, column=0, padx=10, pady=10)
        self.label_senha.grid(row=1, column=0, padx=10, pady=10)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)
        self.entry_senha.grid(row=1, column=1, padx=10, pady=10)
        self.button_login.grid(row=2, columnspan=2, padx=10, pady=10)

    def login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        # Verificar se o usuário e senha estão corretos (simulação básica)
        if usuario == "admin" and senha == "1234":
            messagebox.showinfo("Login", "Login bem-sucedido!")
            # Aqui você pode chamar outra função ou abrir uma nova janela, etc.
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
