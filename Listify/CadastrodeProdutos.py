# Importa o módulo pyodbc para conexão com o banco de dados
import pyodbc

# Importa o módulo tkinter para construção de interfaces gráficas
from tkinter import *

# Importa a classe ttk do módulo tkinter
from tkinter import ttk

# Função qie verifica se as credenciais do usuario estão corretas


def verifica_credenciais():

    # Driver - Driver
    # Server - Servidor
    # Database - Nome do Banco de Dados


    # Com o ChatGPT
    conexao = pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=Projeto_Compras.db")
# Sem o ChatGPT | dadosConexao = "Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db"

 # cursor - Ferramenta para executar comandos SQL
    cursor = conexao.cursor()
    
    #Executando uma query que seleniona os usuarios que possuem o nome de usuario e senha inseridos pelo usuário
    cursor.execute("SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?", (nome_usuario_entry.get(), senha_usuario_entry.get()))

    #Recebendo o resultado da query
    usuario = cursor.fetchone()
    
    # if - se
    if usuario:
        #Destruindo/ Fechando a janela de Login
        janela_principal.destroy()
    

        dadosConexao = "Driver=SQLite3 ODBC Driver;Database=Projeto_Compras.db"

        #Criando a conexao
        conexao = pyodbc.connect(dadosConexao)

        #Cria um objeto cursor papra executar os comandos SQL no banco de dados
        cursor = conexao.cursor()

        #Executa um comando SQL para selecionar todos os valores da tabela de Produtos
        conexao.execute("Select * From Produtos")

        print('Conectado com sucesso')

        def listar_dados():
            
            #Limpa os valores da treeview
            for i in treeview.get_children():
                treeview.delete(i)
                
                #Executa um comando SQL para selecionar todos os valores da tabela de Produtos
            cursor.execute("Select * From Produtos")
            
            #Armazena os valores retornados pelo comando SQL em uma variável
            valores = cursor.fetchall()
            
            # Adiciona os valores na Treeview
            for valor in valores:
                
                #Popula linha por linha
                treeview.insert("", "end", values=(valor[0], valor[1], valor[2], valor[3]))
            
                

        #Criando uma janela tkinter com o título " Cadastro de Produtos"
        janela = Tk()
        janela.title("Cadastro de Produtos")

        #Definindo a cor de fundo para janela
        janela.configure(bg="#F5F5F5")

        #Deixandi a janela em tela cheia
        janela.attributes("-fullscreen", True)

        Label(janela, text="Nome do Produto: " , font= "Arial 16", bg="#F5F5F5").grid(row=0, column=2, padx=10, pady=10)
        nome_produto = Entry(janela, font= "Arial 16" )
        nome_produto.grid(row=0, column=3, padx=10, pady=10)

        Label(janela, text="Descrição do Produto: " , font= "Arial 16", bg="#F5F5F5").grid(row=0, column=5, padx=10, pady=10)
        descricao_produto = Entry(janela, font= "Arial 16" )
        descricao_produto.grid(row=0, column=6, padx=10, pady=10)

        Label(janela, text="Produtos: " , font= "Arial 16",fg="blue", bg="#F5F5F5").grid(row=2, column=0,columnspan=10, padx=10, pady=10)


        #Função para cadastrar um produto
        def cadastrar():
            
            #Cria uma nova janela para cadastrar o produto
            janela_cadastrar = Toplevel(janela)
            janela_cadastrar.title("Cadastrar Produto")

            # bg - background (cor do fundo)
            # Definindo a cor de fundo da janela
            janela_cadastrar.configure(bg="#FFFFFF")

            #Define a largura e altura da janela
            largura_janela = 500
            altura_janela = 200

            #Obtem a largurar e alturar da tela computador
            largura_tela = janela_cadastrar.winfo_screenwidth()
            altura_tela = janela_cadastrar.winfo_screenheight()

            #Calcula a posição da janela para centraliza-la na tela
            """
            Essas linhas calculam a posição em que a janela deve ser
            exibida na tela do computador de foram centralizada.
            A posição x é definida pela diferença entre a largura da tela
            e a largura da janela, dividida por 2. Já a posição y é definida
            pela diferenca entre a altura da tela e a altura da janela, também
            dividida por 2. O PERADOR "//" é utilizado para realizar a divisão 
            inteira, ou seja, retornar apenas o resultado inteiro da divisão.
            """

            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            #Define a posição da janela

            """
            define a geometria da janela principal, especificando a 
            largura e altura da janela, bem como a posição onde a janela 
            será exibida na tela, usando as variáveis previamente definidas
            para a posição x e y da janela. O foromato utilizado é uma string
            que contém os valores de largura,altura,posição x e posição y da
            janela separados por "x" e "+" e passados como argumentos para o método
            geometry() da janela principal

            O formato '{}x{}+{}+{}' é uma string de formatação que espera
            quatro valores, que correspondem À larguras da janela, altura da janela,
            posição x da janela e posição y da janela, respectivamente.

            Esse valores são passados na ordem especificada para a string de formatação
            em seguida, são utlizados para definir a geometria da janela através do 
            método geometry do objeto janela_principal
            """


            janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela,pos_x,pos_y))
        
            for i in range(5):
                janela_cadastrar.grid_rowconfigure(i, weight=1)
                
            for i in range(2):
                janela_cadastrar.grid_columnconfigure(i, weight=1)

            
            #Adiciona bordas para cada campo de entrada
            estilo_borda = {"borderwidth": 2, "relief": "groove"}
            
            # srick - Preenche as laterais NSEW (Norte,Sul,Leste e Oeste)
            # fg - foreground (cor da letra)
            # row - linha
            # column - coluna
            # columnspan - quantas colunas vai ocupar no grid
            # pady - espaçamento

            Label(janela_cadastrar, text="Nome do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, sticky="W")
            nome_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
            nome_produto_cadastrar.grid(row=0,column=1, padx=10, pady=10)
            
            Label(janela_cadastrar, text="Descrição do Produto:", font=("Arial",12), bg="#FFFFFF").grid(row=1,column=0, padx=10, pady=10, stick="W")  
            descricao_produto_cadastrar = Entry(janela_cadastrar,font=("Arial",12), **estilo_borda)
            descricao_produto_cadastrar.grid(row=1,column=1, padx=10, pady=10)
            
            Label(janela_cadastrar, text="Preço do Produto:", font=("Arial",12), bg="#FFFFFF").grid(row=2,column=0, padx=10, pady=10, stick="W")  
            preco_produto_cadastrar = Entry(janela_cadastrar,font=("Arial",12), **estilo_borda)
            preco_produto_cadastrar.grid(row=2,column=1, padx=10, pady=10)


        #Cria uma funçãoi para salvar as funçoes do banco de dados
            def salvar_dados():
                
                #Cria uma tupla com os valores dos campos de texto
                novo_produto_cadastrar = (nome_produto_cadastrar.get(),descricao_produto_cadastrar.get(),preco_produto_cadastrar.get())
                
                
                #Execura um comando SQL para inserir os dados na tabela Produto no Banco de dados
                cursor.execute("INSERT INTO Produtos (NomeProduto, Descricao, Preco) VALUES (?, ?, ?)", novo_produto_cadastrar)
                conexao.commit()

                print("Dados cadasdtrados com sucesso")
                
                #Fecha a janela de cadastrato
                janela_cadastrar.destroy()
                
                listar_dados()
                
        # columnspan - quantas colunas vai ocupar no grid
        # srick - Preenche as laterais NSEW (Norte,Sul,Leste e Oeste)
            botao_salvar_dados = Button(janela_cadastrar, text="Salvar", font=("Arial", 12), command=salvar_dados)
            botao_salvar_dados.grid(row=3, column=0, columnspan=2, padx=10,pady=10, stick="NSEW")
            
            
        # columnspan - quantas colunas vai ocupar no grid
            # srick - Preenche as laterais NSEW (Norte,Sul,Leste e Oeste)
            botao_cancelar = Button(janela_cadastrar, text="Cancelar", font=("Arial", 12), command=janela_cadastrar.destroy)
            botao_cancelar.grid(row=4, column=0, columnspan=2, padx=10,pady=10, stick="NSEW")
            

        #Cria um botão para gravar os dados na tabela Produtos do banco de dados
        botao_gravar = Button(janela, text="Novo", command=cadastrar, font="Arial 26")
        botao_gravar.grid(row=4, column=0, columnspan=4, sticky="NSEW", pady=20, padx=5)


        #Define o estilo da Treeview
        style= ttk.Style(janela)

        #Criando a Treeview
        treeview = ttk.Treeview(janela, style="mystyle.Treeview")

        style.theme_use("default")

        #Configurando
        style.configure("mystyle.Treeview", font=("Arial", 14))

        treeview = ttk.Treeview(janela, style="mystyle.Treeview", columns=("ID", "NomeProduto", "Descricao", "Preco"), show="headings", height=20)

        treeview.heading("ID", text="ID")
        treeview.heading("NomeProduto", text="Nome do Produto")
        treeview.heading("Descricao", text="Descrição do Produto")
        treeview.heading("Preco", text="Preço do Produto")
        #A primeira coluna, identificada como #0
        #A opção "stretch=NO" indica que a coluna não deve esticar para preencher o espaço

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("ID", width=100)
        treeview.column("NomeProduto", width=300)
        treeview.column("Descricao", width=500)
        treeview.column("Preco", width=200)

        # columnspan - quantas colunas vai ocupar no grid
            # srick - Preenche as laterais NSEW (Norte,Sul,Leste e Oeste)
        treeview.grid(row=3,column=0,columnspan=10,sticky="NSEW")

        #Chama a funç]ao para listar os valores do banco de dados na treeview
        listar_dados()

        def editar_dados(event):
            
            #Obtém o item selecionado na Treeview
            item_selecionado = treeview.selection()[0]
            
            #Obtém os valores do item selecionado
            valores_selecionados = treeview.item(item_selecionado)['values']
            
            #Cria uma nova janela para cadastrar o produto
            janela_edicao = Toplevel(janela)
            janela_edicao.title("Editar Produto")

            # bg - background (cor do fundo)
            # Definindo a cor de fundo da janela
            janela_edicao.configure(bg="#FFFFFF")

            #Define a largura e altura da janela
            largura_janela = 550
            altura_janela = 200

            #Obtem a largurar e alturar da tela computador
            largura_tela = janela_edicao.winfo_screenwidth()
            altura_tela = janela_edicao.winfo_screenheight()

            #Calcula a posição da janela para centraliza-la na tela


            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            #Define a posição da janela

            janela_edicao.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela,pos_x,pos_y))
        
            for i in range(5):
                janela_edicao.grid_rowconfigure(i, weight=1)
                
            for i in range(2):
                janela_edicao.grid_columnconfigure(i, weight=1)

            
            #Adiciona bordas para cada campo de entrada
            estilo_borda = {"borderwidth": 2, "relief": "groove"}
            
            # srick - Preenche as laterais NSEW (Norte,Sul,Leste e Oeste)
            # fg - foreground (cor da letra)
            # row - linha
            # column - coluna
            # columnspan - quantas colunas vai ocupar no grid
            # pady - espaçamento

            Label(janela_edicao, text="Nome do Produto:", font=("Arial", 16), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, sticky="W")
            nome_produto_edicao = Entry(janela_edicao, font=("Arial", 16), **estilo_borda, bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[1]))
            nome_produto_edicao.grid(row=0, column=1, padx=10, pady=10)
            
            Label(janela_edicao, text="Descrição do Produto:", font=("Arial",16), bg="#FFFFFF").grid(row=1,column=0, padx=10, pady=10, stick="W")  
            descricao_produto_edicao = Entry(janela_edicao, font=("Arial", 16), **estilo_borda, bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[2]))
            descricao_produto_edicao.grid(row=1,column=1, padx=10, pady=10)
            
            Label(janela_edicao, text="Preço do Produto:", font=("Arial",16), bg="#FFFFFF").grid(row=2,column=0, padx=10, pady=10, stick="W")  
            preco_produto_edicao = Entry(janela_edicao, font=("Arial", 16), **estilo_borda, bg="#FFFFFF",textvariable=StringVar(value=valores_selecionados[3]))
            preco_produto_edicao.grid(row=2,column=1, padx=10, pady=10)


        #Cria uma funçãoi para salvar as funçoes do banco de dados
            def salvar_edicao():
                #Obtém os novos valores do item selecionado no Treeview
                nome_produto = nome_produto_edicao.get()
                nova_descricao = descricao_produto_edicao.get()
                novo_preco = preco_produto_edicao.get()

                # Atualiza os valores do item selecionado
                treeview.item(item_selecionado, values=(valores_selecionados[0], nome_produto, nova_descricao, novo_preco))

                # Executa o comando SQL para atualizar os dados na tabela Produtos no banco de dados
                cursor.execute("UPDATE Produtos SET NomeProduto = ?, Descricao = ?, Preco = ? WHERE ID = ?", (nome_produto, nova_descricao, novo_preco, valores_selecionados[0]))
                conexao.commit()

                
                print("Dados alterados com sucesso")
                
                #Fecha a janela de cadastrato
                janela_edicao.destroy()
                #listar_dados()
                
                
                
            # columnspan - quantas colunas vai ocupar no grid
            # srick - Preenche as laterais NSEW (Norte,Sul,Leste e Oeste)
            botao_salvar_edicao = Button(janela_edicao, text="Alterar", font=("Arial", 12), bg="#008000", fg="#FFFFFF", command=salvar_edicao)
            botao_salvar_edicao.grid(row=4, column=0, padx=20, pady=20)

                
            def deletar_registro():
                
                #Recupera o id do registro selecionado na treeview
                slected_item = treeview.selection()[0]
                id = treeview.item(slected_item)['values'][0]   
                
                #Deleta o registro do banco de dados
                cursor.execute("DELETE FROM Produtos WHERE id = ?", (id))
                
                conexao.commit()
                
                janela_edicao.destroy()
                
                #Recarregar os dados sem o novo resgistro
                listar_dados()
                
            
            
        # columnspan - quantas colunas vai ocupar no grid
            # srick - Preenche as laterais NSEW (Norte,Sul,Leste e Oeste)
            botao_deletar_edicao = Button(janela_edicao, text="Deletar", font=("Arial", 16), bg="#FF0000", fg="#FFFFFF", command=deletar_registro)
            botao_deletar_edicao.grid(row=4, column=1, padx=20,pady=20)
            
            

        #Adicona o evento de duplo clique na Treeview para editar os dados do produtoo
        treeview.bind("<Double-1>", editar_dados)


        #Configura a janela para utilizar a barra de menus criada
        menu_barra = Menu(janela)
        janela.configure(menu=menu_barra)

        #Cria menu chamado Arquivo

        """
        O parametro "tearoff=0" é utilizando no tkinter para controlar
        a exibição de uma linha pontilhada no inicio de menus cascata.
        Ao definir "tearoff=0", a linha pontilhada não será exibida e o
        menu cascata ficará fixo na janela, não podendo ser destacado 
        ou movido para outra posição.
        """
        menu_arquivo = Menu(menu_barra, tearoff=0)
        menu_barra.add_cascade(label="Arquivo",menu=menu_arquivo)

        #Cria um opção no menu "Arquivo" chamada "Cadastrar"
        menu_arquivo.add_command(label="Cadastrar", command=cadastrar)

        #Cria um opção no menu "Arquivo" chamada "Sair"
        menu_arquivo.add_command(label="Sair", command=janela.destroy)

        #Limpo os dados da treeview
        def limparDados():
            # Limpando os valores da treeview
            for i in treeview.get_children():
                # Deleta linha por linha
                treeview.delete(i)

        def filtrar_dados(event=None):
            nome = nome_produto.get()
            descricao = descricao_produto.get()
            
            # Verifica se os campos estão vazios
            if not nome and not descricao:
                listar_dados()
                # Se ambos os campos estiverem vazios, não faz nada
                return

            sql = "SELECT * FROM Produtos"
            params = []

            if nome:
                # Concatena a string 'sql' com a cláusula SQL 'WHERE NomeProduto LIKE ?'
                sql += " WHERE NomeProduto LIKE ?"
                # Adiciona um parâmetro de consulta à lista 'params'
                # O parâmetro é uma string que contém o valor do campo 'nome_produto'
                params.append('%' + nome + '%')

            if descricao:
                if nome:
                    # Se o campo 'nome_produto' também tiver um valor preenchido, adiciona a cláusula 'AND'
                    sql += " AND"
                else:
                    # Se o campo 'nome_produto' não tiver um valor preenchido, adiciona a cláusula 'WHERE'
                    sql += " WHERE"
                # Adiciona a cláusula SQL para filtrar os resultados com base no campo 'descricao_produto'
                sql += " Descricao LIKE ?"
                # Adiciona um parâmetro de consulta para o campo 'descricao_produto'
                params.append('%' + descricao + '%')

            cursor.execute(sql, tuple(params))
            produtos = cursor.fetchall()

            # Limpa os dados da treeview
            limparDados()

            # Preenche treeview com dados filtrados
            for dado in produtos:
                treeview.insert('', 'end', values=(dado[0], dado[1], dado[2], dado[3]))

        nome_produto.bind('<KeyRelease>', filtrar_dados)
        descricao_produto.bind('<KeyRelease>', filtrar_dados)


        #Deleta o registro
        def deletar():
                
                #Recupera o id do registro selecionado na treeview
                slected_item = treeview.selection()[0]
                id = treeview.item(slected_item)['values'][0]   
                
                #Deleta o registro do banco de dados
                cursor.execute("DELETE FROM Produtos WHERE id = ?", (id))
                
                conexao.commit()
            
                #Recarregar os dados sem o novo resgistro
                listar_dados()
                

        #Cria um botão para gravar os dados na tabela Produtos do banco de dados
        botao_deletar = Button(janela, text="Deletar", command=deletar, font="Arial 26")
        botao_deletar.grid(row=4, column=4, columnspan=4, sticky="NSEW", pady=20, padx=5)

        # Inicia a janela Tkinter
        janela.mainloop()

        #Fechar o cursor e a conexao
        cursor.close()
        conexao.close()
                
    else:
        mensagem_lbl = Label(janela_principal,text="Nome de usuáio ou senha incorretos",fg="red")
        mensagem_lbl.grid(row=3,column=0,columnspan=2)


# Função para cadastrar um novo usuário
def cadastrar_novo_usuario():
    novo_nome = nome_usuario_entry.get()
    nova_senha = senha_usuario_entry.get()


    # Limpe os campos de entrada
    nome_usuario_entry.delete(0, 'end')
    senha_usuario_entry.delete(0, 'end')

# Cria a janela principal
janela_principal = Tk()
janela_principal.title("Tela de login")
janela_principal.configure(bg="#F5F5F5")
largura_janela = 450
altura_janela = 260
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)
janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))

titulo_lbl = Label(janela_principal, text="Tela de Login", font="Arial 20", fg="blue", bg="#F5F5F5")
titulo_lbl.grid(row=0, column=0, columnspan=2, pady=20)

nome_usuario_lbl = Label(janela_principal, text="Nome de Usuário", font="Arial 14 bold", bg="#F5F5F5")
nome_usuario_lbl.grid(row=1, column=0, sticky="e")

senha_usuario_lbl = Label(janela_principal, text="Senha", font="Arial 14 bold", bg="#F5F5F5")
senha_usuario_lbl.grid(row=2, column=0, sticky="e")

nome_usuario_entry = Entry(janela_principal, font="Arial 14")
nome_usuario_entry.grid(row=1, column=1, pady=10)

senha_usuario_entry = Entry(janela_principal, show="*", font="Arial 14")
senha_usuario_entry.grid(row=2, column=1, pady=10)

entrar_btn = Button(janela_principal, text="Entrar", font="Arial 14", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")

sair_btn = Button(janela_principal, text="Sair", font="Arial 14", command=janela_principal.destroy)
sair_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")

# Botão para cadastrar novo usuário
cadastrar_usuario_btn = Button(janela_principal, text="Cadastrar Novo Usuário", font="Arial 14", command=cadastrar_novo_usuario)
cadastrar_usuario_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")

for i in range(5):
    janela_principal.grid_rowconfigure(i, weight=1)

for i in range(2):
    janela_principal.grid_columnconfigure(i, weight=1)

janela_principal.mainloop()