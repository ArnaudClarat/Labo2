import sqlite3
from sqlite3 import Error


def menu():
	print("""
	Menu :
		1 : Afficher la liste des bières
		2 : Afficher la liste des softs
		3 : Afficher la liste des boissons chaudes
		4 : Afficher la nombre de produits par catégorie
		5 : Quitter""")


# noinspection PyPep8Naming
def verificateurDeTablePourVoirSiElleExiste():
	nbr = 0
	try:
		cur.execute("SELECT * FROM boissons")
	except Error as e:
		print(e)
		print("Création de la table...")
		cur.execute(
			"CREATE TABLE IF NOT EXISTS boissons (boiID INTEGER PRIMARY KEY, boiNom TEXT, boiCategorie INTEGER)")
		conn.commit()
		with open("data/Boissons.csv") as file:
			for ligne in file:
				boisson, cat = ligne.split(",")
				cur.execute("INSERT INTO boissons (boiNom, boiCategorie) VALUES(?,?)", (boisson, cat))
				nbr += 1
		conn.commit()
		print(nbr, "entrée(s) ajoutée(s).")
	else:
		print("Table déjà créée et remplie.")


def listeBoissons(cat):
	i = 0
	cmd = "SELECT boiNom FROM boissons WHERE boiCategorie = " + cat
	cur.execute(cmd)
	for boisson in cur:
		i += 1
		print(i, boisson[0])


def nbrBoissons():
	cat = ["a", "Bières :", "Softs :", "Boisssons Chaudes :"]
	for i in range(1, 4):
		cmd = "SELECT COUNT (boiNom) FROM boissons WHERE boiCategorie = " + str(i)
		cur.execute(cmd)
		for test in cur:
			print("\t" + cat[i], test[0])


# TODO finir nbrBoissons()


# ---Variables Globales---
choix = "x"
i = 0

# ------Programme-----
try:
	conn = sqlite3.connect("data/Bar")
	cur = conn.cursor()
	print("Connexion réussie!")
except Error as e:
	print(e)

verificateurDeTablePourVoirSiElleExiste()

while choix != "5":
	menu()
	choix = input("Que voulez-vous faire? ").upper()

	if choix == "1":
		listeBoissons(choix)
	if choix == "2":
		listeBoissons(choix)
	if choix == "3":
		listeBoissons(choix)
	if choix == "4":
		nbrBoissons()
