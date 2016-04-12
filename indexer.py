from __future__ import division
import PorterStemmer
import math
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
        self.tfIdf={}
        self.tfIdfQuery={}
        curdoc=0
        
        with open(fn, 'rb') as csvfile:
             spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
             for row in spamreader:

                for token in self.StemTokenizer(row[4]):
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
                        tweet['rating']=row[0]
    
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
                        tweet['rating']=row[0]
    
                        self.terms[token]['tweets'].append(tweet)

                for token in self.StemTokenizer(row[5]):
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
                        tweet['rating']=row[0]

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
                        tweet['rating']=row[0]

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
        score=(-1*neg)+ (1*pos)
        score=score/total
        final = float("{0:.2f}".format(score))
        return final

    def stemming(self, tokens):
        stemmed_tokens = []
        steemer=PorterStemmer.PorterStemmer()
        tempSteemed=""
        for i in tokens:
            tempSteemed=steemer.stem(i,0, len(i)-1)
            stemmed_tokens.append(tempSteemed)
        return stemmed_tokens;

    def StemTokenizer(self,text):
        results=[]
        results=self.stemming(self.tokenize(text))
        return results

    def FindIDF (self, documents, idf ):
        idfScore=math.log10(documents/idf)
        return idfScore
    def FindTF(self, tf):
        if(tf==1):
            tfScore= 1
        elif (tf==0):
            tfScore=0
        else:
            tfScore=1+math.log10(tf)
        return tfScore
    def TfIdf(self, tf, idf):
        return tf*idf

    def docTfIdf(self, tfDic, idfDic):

        for document in tfDic:
            self.tfIdf[document]={}
            for term in idfDic:
                if term in tfDic[document]:
                    self.tfIdf[document][term]=self.TfIdf(self.FindTF(tfDic[document][term]), self.FindIDF(len(tfDic),idfDic[term]))

                else:
                    self.tfIdf[document][term]=0
        return


    def query(self, query):
            tf={}
            idf={}
            numberOfTweets=0
            self.tfIdf={}
            listOfTweets=[]
            search_query = self.StemTokenizer(query)
            score=1
            self.result={}
            self.result["tweets"]=[]

            for term in search_query:
                #print self.terms[term]
                #print self.calcualate_Score(term)

                score = score * self.calcualate_Score(term);
                self.result["score"]=score
#                print self.terms[term]["tweets"]
                for item in self.terms[term]["tweets"]:
                    self.result["tweets"].append(item)

                for tweet in self.result['tweets']:
                  listOfTweets.append(tweet["text"])
            listOfTweets=list(set(listOfTweets)) #remove duplicates
            listOfTweets.append(query)            
            for text in listOfTweets:
                tokens=self.StemTokenizer(text)
                tf[numberOfTweets]={}
                for token in tokens:
                    if token not in tf[numberOfTweets]:
                         tf[numberOfTweets][token]=1
                    else:
                        tf[numberOfTweets][token]+=1
                numberOfTweets+=1
            for i in tf:
                for token in tf[i]:
                    if token in idf:
                        idf[token]+=1
                    else:
                        idf[token]=1
            self.docTfIdf(tf,idf)
            self.tfIdfQuery=self.tfIdf[numberOfTweets-1]
            del self.tfIdf[numberOfTweets-1]
            del listOfTweets[numberOfTweets-1]
            numberOfTweets-=1
            
            self.order = {}
            for i in range(numberOfTweets):
                self.order[i] = self.euclidean(self.tfIdf[i],self.tfIdfQuery)

            #print self.result

            dummyData={}
            dummyData["neg"]={}
            dummyData["pos"]={}
            dummyData["neut"]={}
            dummyData["neg"]['tweet']=[]
            dummyData["pos"]['tweet']=[]
            dummyData["neut"]['tweet']=[]
            dummyData["neg"]['user']=[]
            dummyData["pos"]['user']=[]
            dummyData["neut"]['user']=[]
            dummyData["neg"]['date']=[]
            dummyData["pos"]['date']=[]
            dummyData["neut"]['date']=[]

            for i in sorted(self.order,cmp=self.sort_ord):
                if (self.result['tweets'][i]['rating'] is "4"):
                    dummyData["pos"]['tweet'].append(self.result['tweets'][i]['text'])
                    dummyData["pos"]['date'].append(self.result['tweets'][i]['date'])
                    dummyData["pos"]['user'].append(self.result['tweets'][i]['user'])
                      
                if (self.result['tweets'][i]['rating'] is "2"):
                    dummyData["neut"]['tweet'].append(self.result['tweets'][i]['text'])
                    dummyData["neut"]['date'].append(self.result['tweets'][i]['date'])
                    dummyData["neut"]['user'].append(self.result['tweets'][i]['user'])

                if (self.result['tweets'][i]['rating'] is "0"):
                    dummyData["neg"]['tweet'].append(self.result['tweets'][i]['text'])
  
                
                    dummyData["neg"]['date'].append(self.result['tweets'][i]['date'])
                    dummyData["neg"]['user'].append(self.result['tweets'][i]['user'])

            dummyData["neg"]["rating"] = len(dummyData["neg"]['tweet']) / numberOfTweets;
            dummyData["pos"]["rating"] = len(dummyData["pos"]['tweet']) / numberOfTweets;
            dummyData["neut"]["rating"] = len(dummyData["neut"]['tweet']) / numberOfTweets;

            return dummyData

    def sort_ord(self,x,y):
            z=self.order[x]-self.order[y]
            if z>0.0:
                return 1
            else:
                return -1

    def euclidean(self,doc1, doc2):
            dist=0
            for term in doc1:
                dist+= (doc1[term]-doc2[term])*(doc1[term]-doc2[term])
            return math.sqrt(dist)

                #TODO Add to a result list

            #TODO sort result list by cosine similarity to query
        #TODO transform result list to be usable by GUI


def main(args):
    lookop=LookOP()
    lookop.index("testdata.manual.2009.06.14.csv")
    lookop.query("popular Obama")
    #lookop.index("training.1600000.processed.noemoticon.csv")

if __name__ == "__main__":
    import sys
    main(sys.argv)

