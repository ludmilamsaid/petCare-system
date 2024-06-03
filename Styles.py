def estilo_menu(menu):
    menu.config(
        #bg="lightblue",  # Cor de fundo
        fg="black",      # Cor do texto
        font=("Arial", 12),  # Fonte
        width=30,        # Largura em caracteres
        relief="raised", # Estilo da borda
        highlightthickness=2  # Espessura do destaque
    )
    
def estilo_entry(entry):
    entry.config(
       # bg="lightgray",  # Cor de fundo
        fg="black",      # Cor do texto
        font=("Arial", 12),  # Fonte
        width=90,        # Largura em caracteres
        relief="raised",  # Estilo da borda
        bd=2            # Largura da borda

    )
    
def estilo_botao(button):
    button.config(
        #bg="#4CAF50",     # Cor de fundo
        #fg="white",       # Cor do texto
        font=("Arial", 12),  # Fonte
        width=10,         # Largura em caracteres
        relief="raised",  # Estilo da borda
        bd=2              # Largura da borda
    )