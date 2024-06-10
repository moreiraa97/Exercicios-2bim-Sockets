import asyncio
import websockets

conexao_clientes = {}

async def responder_Cliente(websocket, endereco):
  try:
    nome = await websocket.recv()
    conexao_clientes[nome] = websocket
    async for mensagem in websocket:
      print(f"{nome}: {mensagem}")
      for cliente, ws in conexao_clientes.items():
        if ws != websocket:
          await ws.send(f"{nome}: {mensagem}")
  finally:
    del conexao_clientes[nome]

async def main():
  async with websockets.serve(responder_Cliente, '0.0.0.0',80):
    print("servidor rodando")
    await asyncio.Future()

asyncio.run(main())