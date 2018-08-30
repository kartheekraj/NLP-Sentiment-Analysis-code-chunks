#stop words

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example ='''Grand Theft Auto (GTA) is an action-adventure video game series created by David Jones and Mike Dailly;[2] the later titles of which were created by brothers Dan and Sam Houser, Leslie Benzies and Aaron Garbut. It is primarily developed by Rockstar North (formerly DMA Design), and published by Rockstar Games. The name of the series references the term used in the US for motor vehicle theft.

Most games in the series are set in fictional locales modelled on cities, usually either Liberty City, Vice City or San Andreas, which are stand-ins for New York City, Miami and the state of California, respectively. The first game encompassed three fictional cities, while subsequent titles tend to emphasise a single setting. Gameplay focuses on an open world where the player can choose missions to progress an overall story, as well as engaging in side activities, all consisting of action-adventure, driving, third-person shooting, occasional role-playing, stealth and racing elements. The series focuses around many different protagonists who attempt to rise through the ranks of the criminal underworld, although their motives for doing so vary in each game. The series also has elements of the earlier beat 'em up games from the 16-bit era. The antagonists are commonly characters who have betrayed the protagonist or his organisation, or characters who have the most impact impeding the protagonist's progress. Film and music veterans have voiced characters, including Ray Liotta, Burt Reynolds, Dennis Hopper, Samuel L. Jackson, James Woods, Debbie Harry, Phil Collins, Axl Rose and Peter Fonda.[3] With its British origin, the series contains satire and humour.[4]

British video game developer DMA Design began the series in 1997. As of 2014, it has eleven stand-alone games and four expansion packs. The third chronological title, Grand Theft Auto III, is considered a landmark title, as it brought the series to a 3D setting and more immersive experience. Subsequent titles would follow and build upon the concept established in Grand Theft Auto III, and receive significant acclaim. They subsequently influenced many other open world action games, and led to the label Grand Theft Auto clone on similar games.

The series has been critically acclaimed and commercially successful, having shipped more than 250 million units,[5] making it the fourth-highest selling video game franchise of all time, behind Nintendo's Mario and Pokémon franchises,[6] and Tetris.[7] In 2006, Grand Theft Auto was featured in a list of British design icons in the Great British Design Quest organised by the BBC and the Design Museum.[8] In 2013, The Telegraph ranked Grand Theft Auto among Britain's most successful exports.[4] However, the series has also been controversial for its adult nature and violent themes. '''

stop_words = set(stopwords.words("english"))

#print(stop_words) #prints all the stopwords

words = word_tokenize(example)

'''
filtered_sentence = []

for w in words:
    if w not in  stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)
'''

#Alternative

filtered_sentence = [w for w in words if not w in stop_words]

print(filtered_sentence)

