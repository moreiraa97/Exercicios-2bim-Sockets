import asyncio
import websockets

async def iniciar_cliente(enredeco_url):
    async with websockets.connect(enredeco_url) as websocket:
        nome = input("Entre com o seu nome: ")
        await websocket.send(nome)
        try:
            while True:
                mensagem = input("Entre com a mensagem: ")
                if(mensagem.lower() == 'sair'):
                    break
                await websocket.send(mensagem)
                resposta = await websocket.recv()
                print("Resposta: ", resposta)
        except Exception:
            print("Teve erro")

endereco_servidor = "wss://1deab693-de65-4573-ae66-944caf8136c6-00-narrmx3qefdf.janeway.replit.dev"

asyncio.run(iniciar_cliente(endereco_servidor))