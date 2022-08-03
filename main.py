from pyrogram import Client, filters as f
from os import getenv

TOKEN = getenv("STRING")
EKLENCEK_CHAT_ID = str(getenv("EKLENCEK_CHAT_ID"))

s_k = Client(
	TOKEN,
	api_id="15095702",
	api_hash="a30d70d50032706c7c95a070eaf7c83b"
	)

GONDERILEN = []

@s_k.on_message(f.command("ekleme", ["!", "/", "."]))
async def _(b,m):

	await m.edit("[!!!] Ekleme Başladı!!!")
	print("[!!!] Ekleme Başladı!!!")

	for i in await m.chat.get_members():
		if i.user.id not in GONDERILEN:
			if i.user.status in ["online"]:
				try:
					await b.add_chat_members(EKLENCEK_CHAT_ID, i.user.id)
					GONDERILEN.append(i.user.id)
				except Exception as e:
					print(e)

	await m.edit("[!!!] Üye Ekleme Bitti!!!")
	print("[!!!] Üye Ekleme Bitti!!!")

s_k.run()
