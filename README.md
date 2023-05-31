# TechQuiz
Jogo de perguntas e respostas (“Quizes”) desenvolvido em linguagem Python, para estudantes de CIC (Ciência da Computação) e SI (Sistema de Informação) da Mauá inicialmente.
Já alocados no Jogo, terão 4 “Quizes” que correspondem as disciplinas de Lógica de Programação, Programação Orientada a Objetos, Modelagem Orientada a Objetos e Banco de Dados Relacionais, cada com 10 questões.
Ademais, outra funcionalidade seria os “Quizes Personalizados”, em que os usuários cadastrados como professores, poderão criar “Quizes” sobre diversos assuntos, categorizados como Banco de Dados Relacionais, Programação Orientada a Objetos, Modelagem Orientada a Objetos, Lógica de Programação e outros (poderá registrar nova categoria, ou seja, não se limitando apenas ao curso de CIC e SI). 
## Requisitos
Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:
- Pacote `customtkinter`
- Pacote `requests`
- Pacote `mysql.connector`
- Pacote `pandas`
- Pacote `PIL`
# Instalação
Siga as etapas abaixo para instalar e configurar o projeto:
1. Clone este repositório em sua máquina local:
   ```shell
   git clone https://github.com/TechIMTGroup/TechQuizMaua
   ```
2. Acesse o diretório do projeto:
   ```shell
   cd TechQuizMaua
   ```
3. Instale as dependências do projeto usando o gerenciador de pacotes `pip`:
   ```shell
   pip install -r requirements.txt
   ```


## Instalação do Banco de Dados Local

Para executar o projeto com um banco de dados local, siga as etapas abaixo:

1. Abra o terminal ou prompt de comando.

2. Navegue até o diretório do projeto:

    ```shell
    cd TechQuizMaua
    ```

3. Execute o seguinte comando para importar o arquivo SQL:

    ```shell
    mysql -u username -p database_name < DBTechQuizServer.sql
    ```

    Substitua "username" pelo seu nome de usuário do MySQL e "database_name" pelo nome do banco de dados que deseja usar para o projeto.
    Se necessário, forneça a senha quando solicitado.

4. Navegue até o diretório do projeto:

    ```shell
    cd TechQuizMaua/Local/Codigo
    ```

5. Acesse o arquivo DataBase.py: 

    ```shell
    user = "username"
    password = "password"
    DataBase = "database_name"
    ```

   Substitua "username" pelo seu nome de usuário do MySQL e "database_name" pelo nome do banco de dados que deseja usar para o projeto.
   Se necessário, forneça a senha quando solicitado substituindo "password".


Uma vez que as dependências estejam instaladas e o banco de dados tenha sido criado (se necessário), você estará pronto para executar o projeto.

# Uso
Pode ser feito de duas maneiras, localmente ou em um servidor.
   ## Local

   1. Navegue até o diretório do projeto:

       ```shell
       cd TechQuizMaua/Local
       ```

   2. Execute o arquivo `TechQuiz.py`:

      ```shell
      python TechQuiz.py
      ```

      O programa será iniciado e estará pronto para uso.

   3. Siga as instruções fornecidas pelo programa para interagir com ele.

   ## Online 

   1. Navegue até o diretório do projeto:

       ```shell
       cd TechQuizMaua/Online
       ```

   2. Execute o arquivo `TechQuiz.py`:

      ```shell
      python TechQuiz.py
      ```

      O programa será iniciado e estará pronto para uso.

   3. Siga as instruções fornecidas pelo programa para interagir com ele.

## Contato
  
Se você tiver alguma dúvida ou sugestão sobre o projeto, sinta-se à vontade para entrar em contato:
- Email: felipecarillo@outlook.com
- GitHub: [FelipeCarillo](https://github.com/FelipeCarillo)
