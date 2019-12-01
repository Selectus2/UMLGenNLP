from spacy.lang.en import English

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = English()
# from google.colab import files
# uploaded = files.upload()
with open("Dataset\Self Generated\Text\\2.txt", "r") as myfile:
    data = myfile.readlines()

text = data[0]

#  "nlp" Object is used to create documents with linguistic annotations.
my_doc = nlp(text)

# Create list of word tokens
token_list = []
for token in my_doc:
    token_list.append(token.text)
# print(token_list)

# sentence tokenization


# Load English tokenizer, tagger, parser, NER and word vectors
nlp = English()

# Create the pipeline 'sentencizer' component
sbd = nlp.create_pipe('sentencizer')

# Add the component to the pipeline
nlp.add_pipe(sbd)

# text = """Our auditorium is used for different types of events. Some of the events are one-time events, such as basketball games. Other events consist of a number of shows, such as plays or concerts. The event planner can change the floor plan for each event. Some events use the floor for seating (like concerts) and others do not (like basketball games). All the show seating charts for the same event should be based on the same floor plan. The event planner schedules events and shows. Once an event is negotiated, the event planner decides on the floor plan and schedules the individual shows for the event. Once the shows are scheduled, the event planner prices the shows. Pricing is done using a pricing plan. A pricing plan consists of a set of price tiers. Each price tier contains prices for one or more price types: adult, senior, student, and child. The event planner assigns each price tier to a group of seats in a show, one tier per seat. The event planner may also add one or more discounts to the show to try to improve sales. Customers can purchase seats online. Once they provide us with their mailing address, they can look up shows and select the seats they want to reserve. Customers may pay only by credit card payments. If they want refunds, we will credit the card used to purchase the ticket."""

#  "nlp" Object is used to create documents with linguistic annotations.
doc = nlp(text)

# create list of sentence tokens
sents_list = []
for sent in doc.sents:
    sents_list.append(sent.text)
# print(sents_list)
# print(len(sents_list))
sents_list.insert(0, "Sentence")

import pandas as pd

df = pd.DataFrame(sents_list)
print(df)

csv_data = df.to_csv(index=False)
df.to_csv('filename.csv', index=False)
