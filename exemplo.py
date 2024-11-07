from RevolutionClient import RevolutinClient

client = RevolutinClient(token="")

@client.on_message()
def message(data):
    client.send_message(1854365864210018305, "teste")
    pass

print(client.run())
client.run_handler()