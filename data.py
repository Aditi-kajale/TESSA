from bertopic import BERTopic
# import numpy as np

INPUT_TEXT=""

class NER:  
    selected=False
    output=""
    
    def compute():
        NER.output=INPUT_TEXT[:5]

class SENTIMENT_ANALYSIS:
    selected=False
    output=""
    
    def compute():
        SENTIMENT_ANALYSIS.output=INPUT_TEXT[:5]

class SUMMARIZATION:
    selected=False
    output=""
   
    def compute():
        SUMMARIZATION.output=INPUT_TEXT[:5]

class TOPIC_IDENTIFICATION:
    selected=False
    output=["","",""]
    
    def compute():
        # class CPU_Unpickler(pickle.Unpickler):
        #     def find_class(self, module, name):
        #         if module == 'torch.storage' and name == '_load_from_bytes':
        #             return lambda b: torch.load(io.BytesIO(b), map_location=torch.device('cpu'))
        #         else: return super().find_class(module, name)

        # contents = CPU_Unpickler(open("./models/topicmodel_36NC_2103","rb")).load()

        my_topic_model = BERTopic.load("./models/topicmodel_36NC_0104")
        similar_topics, similarity = my_topic_model.find_topics(INPUT_TEXT, top_n=3)
        # print(f'Top 3 topics: {[(my_topic_model.custom_labels_)[t] for t in similar_topics]}, and the similarities are {np.round(similarity,2)}')
        TOPIC_IDENTIFICATION.output=[(my_topic_model.custom_labels_)[t] for t in similar_topics]
 

