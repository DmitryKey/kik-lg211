import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Mathias Creutz Inc. has acquired Microsoft.')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

