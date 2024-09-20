import pandas as pd
from datasets import Dataset

data = {
    "title": [
        "Pride and Prejudice", "Moby Dick", "The Great Gatsby", "1984", "To Kill a Mockingbird",
        "The Catcher in the Rye", "Brave New World", "The Lord of the Rings", "Harry Potter and the Sorcerer's Stone",
        "Jane Eyre", "The Hobbit", "Fahrenheit 451", "The Picture of Dorian Gray", "Crime and Punishment",
        "The Brothers Karamazov", "The Odyssey", "The Iliad", "War and Peace", "Anna Karenina",
        "Great Expectations", "Dracula", "Frankenstein", "The Alchemist", "Wuthering Heights",
        "The Count of Monte Cristo", "Les Misérables", "Don Quixote", "Madame Bovary", "The Divine Comedy",
        "The Kite Runner", "Memoirs of a Geisha", "The Da Vinci Code", "A Tale of Two Cities",
        "One Hundred Years of Solitude", "Slaughterhouse-Five", "Catch-22", "Of Mice and Men", "Beloved",
        "The Shining", "The Road", "Gone with the Wind"
    ],
    "plot": [
        "The story of Elizabeth Bennet as she navigates love and family dynamics in 19th-century England.",
        "The epic tale of Captain Ahab's obsessive quest to hunt down the great white whale, Moby Dick.",
        "A mysterious millionaire, Jay Gatsby, hosts extravagant parties in hopes of reuniting with his lost love.",
        "In a dystopian future, Winston Smith struggles under the oppressive rule of a totalitarian regime.",
        "Scout Finch grows up in the racially charged American South, learning valuable lessons about justice and morality.",
        "Holden Caulfield, a disillusioned teenager, roams New York after being expelled from prep school.",
        "In a futuristic world, society is divided and controlled, but one man, Bernard Marx, seeks more freedom.",
        "Frodo Baggins embarks on a perilous journey to destroy the One Ring and save Middle-earth.",
        "Young Harry Potter learns he is a wizard and must face the dark forces that threaten the magical world.",
        "Jane Eyre, an orphan, grows up facing harsh treatment and eventually finds love while overcoming personal struggles.",
        "Bilbo Baggins, a hobbit, is thrust into an adventure to help dwarves reclaim their kingdom from a dragon.",
        "In a society where books are banned, Guy Montag, a fireman, begins questioning the purpose of his work.",
        "Dorian Gray remains youthful while a portrait of him ages, reflecting his moral decay.",
        "Raskolnikov, a poor student, commits murder and wrestles with his conscience in St. Petersburg.",
        "Three brothers grapple with faith, morality, and the legacy of their father's sins in this Russian epic.",
        "Odysseus embarks on a long journey home after the Trojan War, facing many obstacles along the way.",
        "The Greek hero Achilles takes part in the Trojan War, seeking glory but ultimately facing tragedy.",
        "The lives of five aristocratic families intersect during Napoleon's invasion of Russia.",
        "Anna Karenina, trapped in a loveless marriage, pursues a tragic love affair with a young officer.",
        "Pip, an orphan, dreams of becoming a gentleman and learning the true nature of love and loyalty.",
        "Jonathan Harker discovers the terrifying truth about Count Dracula, a vampire seeking to spread his curse.",
        "Victor Frankenstein creates a living being, only to be horrified by the consequences of playing God.",
        "Santiago, an Andalusian shepherd, goes on a journey to discover his personal legend and treasure.",
        "Heathcliff and Catherine's intense, destructive relationship plays out on the Yorkshire moors.",
        "Edmond Dantès is wrongfully imprisoned and embarks on a quest for revenge after escaping prison.",
        "Jean Valjean, an ex-convict, seeks redemption amid the political upheavals of post-revolutionary France.",
        "Don Quixote, a man obsessed with chivalric ideals, embarks on misguided adventures with his loyal squire.",
        "Madame Bovary, bored with provincial life, seeks escape through romantic fantasies that lead to her downfall.",
        "Dante journeys through Hell, Purgatory, and Heaven in this epic allegory of the soul's path to God.",
        "Amir recalls his childhood in Afghanistan and his complicated relationship with his best friend, Hassan.",
        "A Japanese woman reflects on her difficult journey from being sold into servitude to becoming a renowned geisha.",
        "Robert Langdon uncovers a secret society while solving a murder mystery related to religious symbols.",
        "The French Revolution brings together the lives of Charles Darnay and Sydney Carton, who both love the same woman.",
        "Magical realism tells the multi-generational story of the Buendía family in the fictional town of Macondo.",
        "Billy Pilgrim, an optometrist, becomes 'unstuck in time' as he recalls his experiences in World War II.",
        "Captain John Yossarian tries to survive the absurdities and horrors of war while facing bureaucratic madness.",
        "George and Lennie, displaced ranch workers during the Great Depression, dream of owning their own farm.",
        "Sethe, an escaped slave, is haunted by her traumatic past and the ghost of her dead daughter.",
        "A family isolated in a haunted hotel during the winter faces terrifying supernatural forces and personal madness.",
        "A father and son journey through a post-apocalyptic landscape, struggling to survive and maintain their humanity.",
        "Scarlett O'Hara's life is upended by the American Civil War as she struggles to maintain her family's plantation."
    ]
}

df = pd.DataFrame(data)

dataset = Dataset.from_pandas(df)

print(dataset)
