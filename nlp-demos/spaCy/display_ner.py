import spacy
from spacy import displacy

text = u"""In 2005, "The Guardian" determined using "estimates of earnings accrued in a composer's lifetime" that George Gershwin was the wealthiest composer of all time. In September 2013, a partnership between the estates of Ira and George Gershwin and the University of Michigan was created and will provide the university's School of Music, Theatre, and Dance access to Gershwin's entire body of work, which includes all of Gershwin's papers, compositional drafts, and scores. This direct access to all of his works will provide opportunities to musicians, composers, and scholars to analyze and reinterpret his work with the goal of accurately reflecting the composers' vision in order to preserve his legacy. The first fascicles of "The Gershwin Critical Edition", edited by Mark Clague, are expected in 2017; they will cover the 1924 jazz band version of "Rhapsody in Blue", "An American in Paris" and "Porgy and Bess"."""

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
displacy.serve(doc, style='ent')
