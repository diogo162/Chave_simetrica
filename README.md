# Chave_simetrica

O código criado em linguagem Python realiza criptografia e descriptografia de mensagens utilizando tabelas de caracteres, sequências binárias únicas e números de identificação de tabela. O algoritmo trabalha em três fases principais: a geração das tabelas de caracteres, a transformação da mensagem original em uma sequência criptografada e a descriptografia dela.

Primeiramente, o programa importa a biblioteca `random`, que será usada para gerar valores aleatórios ao longo do processo. Em seguida, várias funções são definidas para executar tarefas específicas.

A função `generate_key` é responsável pela criação das tabelas de caracteres, que são essenciais para a criptografia. Cada tabela contém uma atribuição aleatória de sequências binárias únicas para representar os caracteres. Essa aleatoriedade aumenta a segurança da criptografia, pois diferentes tabelas têm diferentes comprimentos binários associados a cada caractere.

Outra função é `generate_unique_binaries`, que gera um conjunto de sequências binárias únicas de comprimentos específicos. Essas sequências serão utilizadas posteriormente para representar cada caractere da mensagem criptografada.

A função `assign_binaries_to_characters` é utilizada para a atribuição de sequências binárias únicas a cada caractere nas tabelas de caracteres. Através da seleção aleatória de caracteres e sequências, essa função contribui para reforçar ainda mais a segurança do processo de criptografia.

A etapa de criptografia é realizada pela função `encrypt_message`. Nesse estágio, a mensagem digitada pelo usuário é transformada em uma sequência de caracteres aleatória. O programa seleciona aleatoriamente uma das tabelas de caracteres criadas anteriormente e atribui um ID de tabela a cada caractere da mensagem original. Para isso, o caractere é substituído por sua sequência binária correspondente na tabela selecionada, e o ID de tabela é adicionado no início do caractere criptografado cercado por colchetes de forma que seja facilmente lida por fim de visualização para exemplos. Essa concatenação garante que a mensagem final seja composta por elementos distintos, tornando difícil a identificação do padrão original por um observador externo e virtualmente impossível de um carácter ser falsamente identificado como outro similar.

A fase de descriptografia é realizada pela função `decrypt_message`, que desempenha o papel oposto ao da criptografia. Ela tem a tarefa de reverter o processo e recuperar a mensagem original a partir da mensagem criptografada. Para alcançar esse objetivo, a função utiliza os IDs de tabela presentes no início de cada caractere da mensagem criptografada. Esses IDs são usados para localizar a tabela de caracteres correta que permitirá o mapeamento das sequências binárias de volta aos caracteres originais. Dessa forma, a função percorre a mensagem criptografada, extrai os IDs de tabela e, com base nesses IDs, encontra as sequências binárias correspondentes aos caracteres originais. Consequentemente, a mensagem original é reconstituída e apresentada em sua forma legível.

Após a criptografia ou descriptografia da mensagem, o programa entra em um loop principal que permite a interação contínua com o usuário. Ele pode optar por visualizar as tabelas de caracteres geradas aleatoriamente e, em seguida, digitar a mensagem que deseja criptografar. Após a criptografia, a mensagem criptografada é exibida na tela.

Caso o usuário deseje descriptografar a mensagem, ele tem essa opção. A mensagem descriptografada é então apresentada na tela. O programa ainda questiona se o usuário deseja continuar utilizando o algoritmo, encerrando o loop caso a resposta seja negativa.

Em conclusão, o algoritmo de criptografia e descriptografia implementado em Python é capaz de codificar e decodificar mensagens de forma segura, utilizando tabelas de caracteres e sequências binárias únicas. Através desse processo, a mensagem original é transformada em uma sequência aparentemente aleatória de caracteres criptografados, e pode ser revertida posteriormente para a sua forma original, garantindo a confidencialidade das informações transmitidas. A segurança do algoritmo depende da aleatoriedade das tabelas e sequências binárias geradas, bem como da proteção dos IDs de tabela durante o processo de criptografia e transmissão da mensagem criptografada.

