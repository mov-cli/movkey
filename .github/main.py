import httpx
import click

@click.command()
@click.option("-k", "--key", default=None, help="GHKEY")

def key(key):
    dokicloud = httpx.get("https://api.github.com/repos/consumet/rapidclown/commits/dokicloud", headers={"Authorization": f"Bearer {key}"}).json()
    rabbitstream = httpx.get("https://api.github.com/repos/consumet/rapidclown/commits/rabbitstream", headers={"Authorization": f"Bearer {key}"}).json()
    enimax = httpx.get("ttps://api.github.com/repos/enimax-anime/key/commits/e4", headers={"Authorization": f"Bearer {key}"}).json()
    dokidate = dokicloud["commit"]["author"]["date"]
    rabbitdate = rabbitstream["commit"]["author"]["date"]
    enidate = enimax["commit"]["author"]["date"]
    if dokidate > rabbitdate:
        if dokidate > enidate:
            decryptkey = "https://raw.githubusercontent.com/consumet/rapidclown/dokicloud/key.txt"
        else:
            decryptkey = "https://raw.githubusercontent.com/enimax-anime/key/e4/key.txt"
    else:
        if rabbitdate > enidate:  
            decryptkey = "https://raw.githubusercontent.com/consumet/rapidclown/rabbitstream/key.txt"
        else:
            decryptkey = "https://raw.githubusercontent.com/enimax-anime/key/e4/key.txt"
    u = httpx.get(decryptkey).text
    with open(f"key.txt", "w") as f:
        f.write(u)

if __name__ == '__main__':
    key()
