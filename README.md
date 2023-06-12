# TechQuiz
Jogo de perguntas e respostas (“Quizes”) desenvolvido em linguagem Python, para estudantes de CIC (Ciência da Computação) e SI (Sistema de Informação) da Mauá inicialmente.
Já alocados no Jogo, terão 4 “Quizes” que correspondem as disciplinas de Lógica de Programação, Programação Orientada a Objetos, Modelagem Orientada a Objetos e Banco de Dados Relacionais, cada com 10 questões.
Ademais, outra funcionalidade seria os “Quizes Personalizados”, em que os usuários cadastrados como professores, poderão criar “Quizes” sobre diversos assuntos, categorizados como Banco de Dados Relacionais, Programação Orientada a Objetos, Modelagem Orientada a Objetos, Lógica de Programação e outros (poderá registrar nova categoria, ou seja, não se limitando apenas ao curso de CIC e SI). 
## Requisitos
Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:
- `Python` --> [INSTALAÇÃO](https://python.org.br/instalacao-windows/)
- DBMS `Mysql` --> [INSTALAÇÃO](https://www.alura.com.br/artigos/mysql-do-download-e-instalacao-ate-sua-primeira-tabela)
- Pacote `tkinter`
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
    .. /TechQuizMaua
    ```
3. Execute o seguinte comando para criar um DataBase:
    
    ```shell
    mysql -u "username" -p -e "CREATE DATABASE dbTechQuiz2023"
    ```
    Substitua "username" pelo seu nome de usuário do MySQL.
    Se necessário, forneça a senha quando solicitado.
5. Execute o seguinte comando para importar o arquivo SQL:

    ```shell
    mysql -u "username"-p dbTechQuiz2023 < dbTechQuiz.sql
    ```
    Substitua "username" pelo seu nome de usuário do MySQL.
    Se necessário, forneça a senha quando solicitado.

4. Navegue até o diretório do projeto:

    ```shell
    .. /TechQuizMaua
    ```
5. Acesse o arquivo AcessoDB.txt: 

    ```shell
    username -- password
    ```
   Substitua "username" pelo seu nome de usuário do MySQL e forneça a senha substituindo "password".
   
   Exemplo:
   ```shell
    Tech -- Quiz
    ```
   ## Opicional
      Para a execução da parte administrativa do Jogo Local é necessário a utilização de uma API_KEY da [OPENAI](https://platform.openai.com/account/api-keys), para a implementação da chave acesse o arquvio txt do diretorio:
      ```shell
       TechQuizMaua/APIKEY.txt
      ```
      E dentro dele substitua o "API_KEY_AQUI" pela sua respectiva chave.
 
Uma vez que as dependências estejam instaladas e o banco de dados tenha sido criado (se necessário), você estará pronto para executar o projeto.

# Uso
Pode ser feito de duas maneiras, localmente ou em um servidor.
   ## Local

   1. Navegue até o diretório do projeto:

       ```shell
       .. /TechQuizMaua
       ```
   2. Execute o arquivo `TechQuiz.py`:

      ```shell
      python TechQuizLocal.py
      ```
      O programa será iniciado e estará pronto para uso.

   3. Siga as instruções fornecidas pelo programa para interagir com ele.

   ## Online 

   1. Navegue até o diretório do projeto:

       ```shell
       .. /TechQuizMaua
       ```
   2. Execute o arquivo `TechQuiz.py`:

      ```shell
      python TechQuizOnline.py
      ```
      O programa será iniciado e estará pronto para uso.

   3. Siga as instruções fornecidas pelo programa para interagir com ele.

## Contato
  
Se você tiver alguma dúvida ou sugestão sobre o projeto, sinta-se à vontade para entrar em contato:
- Email: felipecarillo@outlook.com
- GitHub: [FelipeCarillo](https://github.com/FelipeCarillo)

