import asyncio
import discord

with open("tokens.txt", "r", encoding="utf-8") as f:
    TOKENS = [x.strip() for x in f if x.strip()]

async def start_lxc(token):
    lxc = discord.Client()

    @lxc.event
    async def on_ready():
        print(f"[+] {lxc.user} | {lxc.user.id}")

    try:
        await lxc.start(token)
    except Exception as e:
        print(f"[!] Client failed: {e}")

async def main():
    if not TOKENS:
        print("[!] tokens.txt is empty")
        return
    await asyncio.gather(*(start_lxc(token) for token in TOKENS))

if __name__ == "__main__":
    asyncio.run(main())
