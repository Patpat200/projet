
questions = [
    {
        "question": "Quel est le capital de France?",
        "choices": ["Paris", "Londres", "Berlin", "Rome"],
        "correct": "Paris"
    },
    {
        "question": "Quel est le plus grand pays du monde?",
        "choices": ["Etats-Unis", "Chine", "Russie", "Canadà"],
        "correct": "Russie"
    },
    {
        "question": "Quel est le plus petit pays du monde?",
        "choices": ["Vatican", "Monaco", "Nauru", "Tuvalu"],
        "correct": "Vatican"
    },
    {
        "question": "Comment je m'appelle ?",
        "choices": ["Tacos", "Elon Musk", "Jean", "Macron"],
        "correct": "Elon Musk"
    },
    {
        "question": "Qui a écrit Les Miserables?",
        "choices": ["Victor Hugo", "Alexandre Dumas", "Emile Zola", "Gustave Flaubert"],
        "correct": "Victor Hugo"
    },
    {
        "question": "Quel est le plus grand océan du monde?",
        "choices": ["Atlantique", "Pacifique", "Indien", "Arctique"],
        "correct": "Pacifique"
    },
    {
        "question": "Qui a peint La Nuit étoilée?",
        "choices": ["Pablo Picasso", "Claude Monet", "Edvard Munch", "Vincent van Gogh"],
        "correct": "Vincent van Gogh"
    },
    {
        "question": "Quel est le plus haut sommet de l'Afrique?",
        "choices": ["Mont Kenya", "Mont Elgon", "Mont Kilimandjaro", "Mont Rwenzori"],
        "correct": "Mont Kilimandjaro"
    },
    {
        "question": "Quel est la capitale de l'Allemagne ?",
        "choices": ["Paris", "Dubaï", "Berlin", "le Listenbourg"],
        "correct": "Berlin"
    },
    {
        "question": "Quel est le plus grand pays d'Europe en termes de superficie?",
        "choices": ["Allemagne", "France", "Espagne", "Ukraine"],
        "correct": "Ukraine"
    },
    {
        "question": "Quel est le plus long fleuve d'Asie?",
        "choices": ["Le Yangtze", "Le Gange", "Le Mékong", "Le Brahmapoutre"],
        "correct": "Le Yangtze"
    }
]
username = input("Entrez votre nom d'utilisateur : ")
while True:
    score = 0
    for question in questions:
        print(question["question"])
        for i, choice in enumerate(question["choices"]):
            print(f"{i + 1}. {choice}")
        answer = input("Entrez le numéro de votre réponse : ")
        if question["choices"][int(answer) - 1] == question["correct"]:
            print("\033[32mBonne réponse!\033[0m")
            score += 1
        else:
            print("\033[91mMauvaise réponse.\033[0m")
            print("La réponse correcte était : ",question["correct"])

    print(f"Bravo {username} ton score est de {score} sur {len(questions)}.")
    if input("Voulez-vous rejouer? (oui/non)").lower() == "non":
        break



