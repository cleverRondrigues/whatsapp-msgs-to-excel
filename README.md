# Automação de Envio de Mensagens no WhatsApp com PyWhatKit

Este projeto automatiza o envio de mensagens pelo WhatsApp utilizando a biblioteca `pywhatkit`. O código permite cadastrar pessoas, armazenar suas informações em uma planilha Excel e enviar mensagens de maneira automatizada para todos os contatos salvos.

## Funcionalidades

- Cadastrar pessoas (nome, idade e número de telefone).
- Validar e formatar os números de telefone antes de enviar as mensagens.
- Salvar os dados cadastrados em uma planilha Excel (`meu_arquivo.xlsx`).
- Enviar mensagens automatizadas para todos os contatos salvos.
- Notificar quando a tarefa for concluída usando o `win10toast`.
- Fechar o WhatsApp Web após cada envio para evitar problemas de repetição de mensagens.

## Tecnologias Utilizadas

- **Python** 🐍
- **PyWhatKit** (para automação de envio de mensagens)
- **PyAutoGUI** (para controlar a interface do WhatsApp Web)
- **Pandas** (para manipulação dos dados)
- **Win10Toast** (para notificações no Windows)

## Como Usar

### Instalar as Dependências

Antes de rodar o código, instale as bibliotecas necessárias:

```bash
pip install pywhatkit pyautogui pandas openpyxl win10toast
```

### Executar o Código

No terminal, execute:

```bash
python whatsapp-msgs-to-excel-main.py
```

### Interação com o Código

- O programa solicitará o nome, a idade e o número de telefone de cada pessoa.
- Você pode continuar adicionando pessoas ou, ao final, optar por salvar as informações em uma planilha Excel.
- Após isso, você será perguntado se deseja enviar mensagens para os números cadastrados.
- O WhatsApp Web será usado para enviar as mensagens automaticamente.
  
### Notificação de Tarefa Concluída

Quando todas as mensagens forem enviadas, uma notificação será exibida no seu computador indicando que a tarefa foi concluída com sucesso.

## Observações Importantes

- **WhatsApp Web precisa estar aberto e logado** no navegador. O código vai usar a interface web para enviar as mensagens.
- A função `sendwhatmsg_instantly` pode levar alguns segundos para enviar a mensagem, então o código aguarda entre cada envio para garantir que o WhatsApp Web processe corretamente.
- Os números de telefone devem estar no formato internacional (ex: +55 para Brasil), sem espaços ou hífens.
- O código fecha a aba do WhatsApp Web automaticamente após o envio de cada mensagem, para evitar que as mensagens sejam enviadas repetidamente para o mesmo número.

## Contribuindo

Se você encontrar algum erro ou quiser sugerir melhorias, fique à vontade para abrir uma **Issue** ou até mesmo contribuir para o projeto com um **Pull Request**.

## Contato

Caso tenha dúvidas, sinta-se à vontade para entrar em contato ou abrir uma nova issue.

```
