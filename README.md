# Projeto IoT com ESP32 e ThingSpeak

Este projeto demonstra como utilizar o microcontrolador ESP32 em conjunto com a plataforma **ThingSpeak** para coleta e envio de dados analógicos via Wi-Fi. O ambiente de simulação utilizado é o [Wokwi](https://wokwi.com), que permite testar todo o sistema virtualmente, sem necessidade de hardware físico.

## 📂 Estrutura

- `main.py`: Código principal do projeto implementado em C++ para a plataforma Arduino.
- Ambiente simulado no Wokwi com ESP32 e potenciômetro (slider).

## 🚀 Objetivo

Ler valores analógicos de um potenciômetro conectado ao pino **GPIO34** do ESP32, e enviá-los periodicamente (a cada 15 segundos) para um canal no **ThingSpeak**, utilizando o protocolo HTTP.

## 🔧 Requisitos

- Conta na plataforma [ThingSpeak](https://thingspeak.com)
- Canal criado com pelo menos um campo de dados (`field1`)
- **Chave de API** gerada pelo ThingSpeak
- Acesso ao simulador [Wokwi](https://wokwi.com)
- Biblioteca `WiFi.h` e `HTTPClient.h` disponíveis via Arduino IDE

## 🧠 Funcionamento

1. Conexão à rede Wi-Fi simulada **Wokwi-GUEST** (sem senha).
2. Leitura de valores analógicos do pino **GPIO34**.
3. Envio dos dados para o ThingSpeak usando uma requisição HTTP `GET`.
4. Repetição do processo a cada 15 segundos, respeitando os limites da plataforma.

## 💻 Execução no Wokwi

1. Acesse o site [https://wokwi.com](https://wokwi.com)
2. Crie um novo projeto com ESP32.
3. Copie e cole o conteúdo de `main.py` no editor.
4. Substitua `SUA_API_KEY` pela sua chave de API do ThingSpeak.
5. Clique em "Start Simulation".

## 🌐 Formato da Requisição HTTP

A URL para envio dos dados segue o seguinte formato:

```

[http://api.thingspeak.com/update?api\_key=SUA\_API\_KEY\&field1=VALOR](http://api.thingspeak.com/update?api_key=SUA_API_KEY&field1=VALOR)

```

Onde:
- `SUA_API_KEY`: sua chave de escrita do canal ThingSpeak
- `VALOR`: valor lido do ADC (0 a 4095)

## 📊 Visualização

Os dados enviados podem ser visualizados no painel do seu canal no ThingSpeak, com gráficos automáticos para interpretação da variável lida.

## 📘 Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo `LICENSE` para mais informações.
```
