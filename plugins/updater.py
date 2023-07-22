import sys
import asyncio
import shlex
from typing import Tuple
from os import environ, execle, path, remove
from pyrogram import Client, filters
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
frm rsrconfig import Config


async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )



@Client.on_message(filters.command("update", prefixes=[".", ","]) & (filters.me | filters.user(Config.SUDO)))
async def mzupdate(client, message):
    try:
        repo = Repo()
    except GitCommandError:
        return await mesage.reply(
            "Harsatna engemaw vangin ka in update theilo."
        )
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "upstream" in repo.remotes:
            origin = repo.remote("upstream")
        else:
            origin = repo.create_remote("upstream", "(I repo link)") # (I repo link) tih aiah hian i repository link, private emaw public kha i hman dan a zirin dah mai tur
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    try:
        repo.create_remote("upstream", "(I repo link)") # (I repo link) tih aiah hian i repository link, private emaw public kha i hman dan a zirin dah mai tur
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch("main")
    try:
        ups_rem.pull("main")
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await run_cmd("pip3 install -r requirements.txt")
    args = [sys.executable, "bot.py"]
    execle(sys.executable, *args, environ)
    exit()
    return
