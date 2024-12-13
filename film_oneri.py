import random

film_veritabani = [
    {"ad": "The Godfather", "turler": ["suç", "gerilim", "macera"]},
    {"ad": "Pulp Fiction", "turler": ["suç", "gerilim", "komedi"]},
    {"ad": "The Dark Knight", "turler": ["aksiyon", "suç", "gerilim"]},
    {"ad": "The Lion King", "turler": ["animasyon", "aile", "macera"]},
    {"ad": "Avatar", "turler": ["aksiyon", "macera", "fantastik"]},
    {"ad": "Toy Story", "turler": ["animasyon", "aile", "komedi"]},
    {"ad": "Gladiator", "turler": ["aksiyon", "tarih", "macera"]},
    {"ad": "The Matrix", "turler": ["aksiyon", "gerilim", "fantastik"]},
    {"ad": "The Avengers", "turler": ["aksiyon", "süper kahraman", "macera"]},
    {"ad": "Forrest Gump", "turler": ["komedi", "romantik", "tarih"]},
    {"ad": "The Terminator", "turler": ["aksiyon", "gerilim", "sci-fi"]},
    {"ad": "Jurassic Park", "turler": ["aksiyon", "macera", "bilim kurgu"]},
    {"ad": "Inception", "turler": ["gerilim", "aksiyon", "psikolojik"]},
    {"ad": "Back to the Future", "turler": ["macera", "komedi", "bilim kurgu"]},
    {"ad": "Jaws", "turler": ["gerilim", "korku", "macera"]},
    {"ad": "The Lord of the Rings: The Fellowship of the Ring", "turler": ["fantastik", "macera", "aksiyon"]},
    {"ad": "Deadpool", "turler": ["aksiyon", "komedi", "süper kahraman"]},
    {"ad": "The Prestige", "turler": ["gerilim", "mystery", "psikolojik"]},
    {"ad": "Mad Max: Fury Road", "turler": ["aksiyon", "macera", "gerilim"]},
    {"ad": "The Incredibles", "turler": ["animasyon", "aksiyon", "aile"]},
    {"ad": "Shrek", "turler": ["animasyon", "komedi", "aile"]},
    {"ad": "The Hunger Games", "turler": ["aksiyon", "macera", "gerilim"]},
    {"ad": "Coco", "turler": ["animasyon", "müzikal", "aile"]},
    {"ad": "The Grand Budapest Hotel", "turler": ["komedi", "macera", "dram"]},
    {"ad": "Guardians of the Galaxy", "turler": ["aksiyon", "bilim kurgu", "komedi"]},
    {"ad": "The Witcher", "turler": ["fantastik", "aksiyon", "macera"]},
    {"ad": "Zootopia", "turler": ["animasyon", "macera", "komedi"]},
    {"ad": "Finding Nemo", "turler": ["animasyon", "macera", "aile"]},
    {"ad": "The Exorcist", "turler": ["gerilim", "korku"]},
    {"ad": "The Conjuring", "turler": ["gerilim", "korku"]},
    {"ad": "It", "turler": ["korku", "gerilim"]},
    {"ad": "Toy Story 3", "turler": ["animasyon", "aile", "komedi"]},
    {"ad": "The Fault in Our Stars", "turler": ["romantik", "drama"]},
    {"ad": "La La Land", "turler": ["romantik", "müzikal", "drama"]},
    {"ad": "The Godfather: Part II", "turler": ["suç", "gerilim", "drama"]},
    {"ad": "Fight Club", "turler": ["gerilim", "psikolojik", "aksiyon"]},
    {"ad": "The Shining", "turler": ["korku", "gerilim"]},
    {"ad": "A Quiet Place", "turler": ["gerilim", "korku"]},
    {"ad": "Whiplash", "turler": ["drama", "müzikal"]},
    {"ad": "Blade Runner 2049", "turler": ["aksiyon", "bilim kurgu", "gerilim"]},
    {"ad": "The Big Lebowski", "turler": ["komedi", "suç", "dram"]},
    {"ad": "The Departed", "turler": ["suç", "gerilim", "aksiyon"]},
    {"ad": "Jumanji", "turler": ["macera", "komedi", "aile"]},
    {"ad": "Star Wars: A New Hope", "turler": ["aksiyon", "macera", "bilim kurgu"]},
    {"ad": "Pirates of the Caribbean: The Curse of the Black Pearl", "turler": ["aksiyon", "macera", "komedi"]},
    {"ad": "Deadpool 2", "turler": ["aksiyon", "komedi", "süper kahraman"]},
    {"ad": "Pacific Rim", "turler": ["aksiyon", "bilim kurgu", "gerilim"]},
    {"ad": "Casino Royale", "turler": ["aksiyon", "gerilim", "suç"]},
    {"ad": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "turler": ["fantastik", "macera", "aile"]},
    {"ad": "WALL-E", "turler": ["animasyon", "bilim kurgu", "romantik"]},
    {"ad": "How to Train Your Dragon", "turler": ["animasyon", "aile", "macera"]},
    {"ad": "Django Unchained", "turler": ["western", "drama", "gerilim"]},
    {"ad": "The Green Mile", "turler": ["dram", "fantastik", "suç"]},
    {"ad": "Interstellar", "turler": ["bilim kurgu", "drama", "macera"]},
    {"ad": "The Wolf of Wall Street", "turler": ["komedi", "dram", "biyografi"]},
    {"ad": "12 Years a Slave", "turler": ["tarih", "dram", "biyografi"]},
    {"ad": "Life of Pi", "turler": ["macera", "dram", "fantastik"]},
    {"ad": "The Revenant", "turler": ["macera", "dram", "tarih"]},
    {"ad": "Harry Potter and the Philosopher's Stone", "turler": ["fantastik", "macera", "aile"]},
    {"ad": "Frozen", "turler": ["animasyon", "aile", "müzikal"]},
    {"ad": "The Notebook", "turler": ["romantik", "dram"]},
    {"ad": "Braveheart", "turler": ["tarih", "dram", "savaş"]},
    {"ad": "Cast Away", "turler": ["dram", "macera"]},
    {"ad": "300", "turler": ["aksiyon", "savaş", "tarih"]},
]


kullanici_turu = input("Hangi türde film izlemek istersiniz? (Örnek: aksiyon, komedi, romantik, korku, animasyon): ").lower()

onerilen_filmler = [film["ad"] for film in film_veritabani if any(tur in film["turler"] for tur in kullanici_turu.split(", "))]

if onerilen_filmler:
    print(f"\n{len(onerilen_filmler)} adet öneri bulundu:")
    for film in onerilen_filmler:
        print(f"- {film}")
    
    rastgele_film = random.choice(onerilen_filmler)
    print(f"\nRastgele öneri: {rastgele_film}")
else:
    print("\nMaalesef, istediğiniz türde film bulunamadı.")
