from __future__ import division
class LookOP(object):
    def __init__(self):
        self.terms={}

    def tokenize(self, text):
        import re
        clean_string = re.sub('[^a-z0-9 ]', ' ', text.lower())
        tokens = clean_string.split()
        return tokens


    def index(self,fn):
        import csv
        self.terms={}
        self.result={}
        self.documents={}
        curdoc=0
        
        with open(fn, 'rb') as csvfile:
             spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
             for row in spamreader:

                for token in self.tokenize(row[4]):
                    if token not in self.terms:
                        self.terms[token]={}
                        self.terms[token]['tf']=1
                        self.terms[token]['pos']=0
                        self.terms[token]['neut']=0
                        self.terms[token]['neg']=0
                        self.terms[token]['tweets']=[]
                        tweet = {}
                        tweet['date']=row[2]
                        tweet['text']=row[5]
                        tweet['user']=row[4]
    
                        self.terms[token]['tweets'].append(tweet)

                        if row[0]=="4":
                            self.terms[token]['pos']=1
                        if row[0]=="2":
                            self.terms[token]['neut']=1
                        if row[0]=="0":
                            self.terms[token]['neg']=1
                    else:                        
                        self.terms[token]['tf']+=1
                        if row[0]=="4":
                            self.terms[token]['pos']+=1
                        if row[0]=="2":
                            self.terms[token]['neut']+=1
                        if row[0]=="0":
                            self.terms[token]['neg']+=1

                        tweet = {}
                        tweet['date']=row[2]
                        tweet['text']=row[5]
                        tweet['user']=row[4]
    
                        self.terms[token]['tweets'].append(tweet)

                for token in self.tokenize(row[5]):
                    if token not in self.terms:
                        self.terms[token]={}                            
                        self.terms[token]['tf']=1
                        self.terms[token]['pos']=0
                        self.terms[token]['neut']=0
                        self.terms[token]['neg']=0
                        self.terms[token]['tweets']=[]
                        tweet = {}
                        tweet['date']=row[2]
                        tweet['text']=row[5]
                        tweet['user']=row[4]

                        self.terms[token]['tweets'].append(tweet)

                        if row[0] == "4":
                            self.terms[token]['pos']=1
                        if row[0] is "2":
                            self.terms[token]['neut']=1
                        if row[0] is "0":
                            self.terms[token]['neg']=1
                    else:
                        self.terms[token]['tf']+=1
                        if row[0] is "4":
                            self.terms[token]['pos']+=1
                        if row[0] is "2":
                            self.terms[token]['neut']+=1
                        if row[0] is "0":
                            self.terms[token]['neg']+=1

                        tweet = {}
                        tweet['date']=row[2]
                        tweet['text']=row[5]
                        tweet['user']=row[4]

                        self.terms[token]['tweets'].append(tweet)

        #print self.terms['Obama']
        #print self.terms['kindle']
    def calcualate_Score(self,term):
        #I CHOSE -5 0 5 to calculate the final score so we can display, we need to discuss this
        score=0
        a=self.terms[term]
        neg=self.terms[term]['neg']
        pos=self.terms[term]['pos']
        total=self.terms[term]['tf']
        score=(-5*neg)+ (5*pos)
        score=score/total
        final = float("{0:.2f}".format(score))
        return final
    def query(self, query):
            search_query = self.tokenize(query)
            for term in search_query:
                #print self.terms[term]
                print self.calcualate_Score(term)
                self.result[term]={}
                self.result[term]["score"]=self.calcualate_Score(term)
                self.result[term]["tweets"]=self.terms[term]["tweets"]
                print self.result[term]



                #TODO Add to a result list

            #TODO sort result list by cosine similarity to query
        #TODO transform result list to be usable by GUI

    def cosine(self,searchText,text):

        return

def main(args):
    lookop=LookOP()
    lookop.index("testdata.manual.2009.06.14.csv")
    lookop.query("Obama")
    #lookop.index("training.1600000.processed.noemoticon.csv")

if __name__ == "__main__":
    import sys
    main(sys.argv)

