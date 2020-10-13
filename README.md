# EnvironmentChecker


## What is it for:

The EnvironmentChecker script provides a tabular report on the computer's terminal, to check the tools necessary for you to maintain an equal development environment between different machines, and also to validate whether the necessary programs for the execution of a project are available locally and with the correct versions.


## How it works:

The requirements.json file contains a list of user-defined programs, and within each niche is the name of the program and the version of the program that the user expects to have installed on his machine. This list can be shared by different members of a team, even if each member needs different programs and different versions of programs, because the "required" option of the json file informs if the installation of that program should be checked or not. If it is true, the script will check the installation, if it is false, it will not.
In this way, the same list can be shared without the need to remove any items, just by changing the values ​​of true and false in the required key.


## How does the script scan different programs?

Inside the json file, there is a "check_cmd" key, which contains the terminal command that will be used to check whether the program is installed or not. This command is provided by the user, and changes according to the type of program. But once the user knows what command is needed to verify its installation, just write it in the key "check_cmd", and the script will read that command and execute it, checking if the program is installed and which version is installed.



# EnvironmentChecker (PT-BR)



## Para que serve:

O script EnvironmentChecker fornece um relatório em forma de tabela no terminal do computador, para uma verificação das ferramentas necessárias para que você mantenha um ambiente de desenvolvimento igual entre diversas máquinas, e também para validar se os programas necessários para a execução de um projeto estão disponíveis localmente e com as versões corretas.


## Como funciona:

O arquivo requirements.json contém uma lista de programas definidos pelo usuário, e dentro de cada nicho está o nome do programa e a versão do programa que o usuário espera ter instalado em sua máquina. Essa lista pode ser compartilhada por diferentes membros de um time, mesmo que cada membro necessite de programas diferentes e versões de programas diferentes, pois a opção "required" do arquivo json informa se a instalação daquele programa deve ser verifica ou não. Se estiver como true, o script irá verificar a instalação, se estiver como false, não irá.
Dessa forma, uma mesma lista pode ser compartilhada sem a necessidade de remover nenhum item,  apenas mudando os valores de true e false na chave required.


## Como o script consegue fazer a varredura de diferentes programas?

Dentro do arquivo json, tem uma chave "check_cmd", que contém o comando de terminal que será usado para verificar se o programa está instalado ou não. Esse comando é fornecido pelo usuário, e muda de acordo com o tipo de programa. Mas uma vez que o usuário sabe qual é o comando necessário para verificar sua instalação, basta escreve-lo na chave "check_cmd", e o script irá ler esse comando e executar, verificando se o programa está instalado e qual é a versão instalada.
