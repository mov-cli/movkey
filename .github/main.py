import httpx

dokicloud = httpx.get("https://api.github.com/repos/consumet/rapidclown/commits/dokicloud").json()
rabbitstream = httpx.get("https://api.github.com/repos/consumet/rapidclown/commits/rabbitstream").json()
dokidate = dokicloud["commit"]["author"]["date"]
rabbitdate = rabbitstream["commit"]["author"]["date"]
if dokidate > rabbitdate:
    decryptkey = "https://raw.githubusercontent.com/consumet/rapidclown/dokicloud/key.txt"
else:
    decryptkey = "https://raw.githubusercontent.com/consumet/rapidclown/rabbitstream/key.txt"
u = httpx.get(decryptkey).text
with open(f"key.txt", "w") as f:
    f.write(u)
