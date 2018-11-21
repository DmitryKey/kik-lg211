import spacy
from spacy import displacy

text = u"""With a degree of frustration, George tried various piano teachers for some two years (circa. 1911) before finally being introduced to Charles Hambitzer by Jack Miller (circa. 1913), the pianist in the Beethoven Symphony Orchestra. Until his death in 1918, Hambitzer remained Gershwin's musical mentor and taught him conventional piano technique, introduced him to music of the European classical tradition, and encouraged him to attend orchestral concerts. Following such concerts, young Gershwin would essentially try to play, on the piano at home, the music he had heard from recall, and without sheet music. As a matter of course, Gershwin later studied with the classical composer Rubin Goldmark and avant-garde composer-theorist Henry Cowell, thus formalizing his classical music training.

In 1913, Gershwin left school at the age of 15 and found his first job as a "song plugger". His employer was Jerome H. Remick and Company, a Detroit-based publishing firm with a branch office on New York City's Tin Pan Alley, and he earned $15 a week.
"""

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
displacy.serve(doc, style='ent')
