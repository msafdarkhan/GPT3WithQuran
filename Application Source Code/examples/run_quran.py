import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

gpt = GPT(temperature=0.5, max_tokens=500)
#Surah Al-Fatiha
gpt.add_example(Example(
    "About: prayer for the guidance, lordship and mercy of God",
    "In the name of God, the infinitely Compassionate and Merciful. Praise be to God, Lord of all the worlds. The Compassionate, the Merciful. Ruler on the Day of Reckoning. You alone do we worship, and You alone do we ask for help. Guide us on the straight path, the path of those who have received your grace; not the path of those who have brought down wrath, nor of those who wander astray. Amen."
))
#Ayat Al-Kursi
gpt.add_example(Example(
    "About: nothing and nobody is regarded to be comparable to Allah",
    "Allah! There is no god but He – the Living, The Self-subsisting, Eternal. No slumber can seize Him Nor Sleep. His are all things In the heavens and on earth. Who is there can intercede In His presence except As he permitteth? He knoweth What (appeareth to His creatures As) Before or After or Behind them. Nor shall they encompass Aught of his knowledge Except as He willeth. His throne doth extend Over the heavens And on earth, and He feeleth No fatigue in guarding And preserving them, For He is the Most High. The Supreme (in glory)."
))
#Perspective
gpt.add_example(Example(
    "About: perspective about our lives",
    "the life of this world is only the enjoyment of deception"
))
#patience
gpt.add_example(Example(
    "About: patience",
    "allah does not burden a soul beyond that it can bear"
))

config = UIConfig(description= "After Listing Quran some point of views from GPT3",
                  button_text= "Point of View",
                  placeholder= "About: ")

demo_web_app(gpt, config)
