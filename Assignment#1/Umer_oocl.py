#Name: Muhammad Umer Fiaz
#SID: 1727123
#CCID: mufiaz
#AnonID: 1000334845
#CMPUT 274, Fall 2022
 
#Assessment: Assignment 1

#Running instructions: 

#Notes and Assumptions:
#    Acknowledgements: Heteng Mehta helped me in a little bit of the codes, Ohm Panchai & Eric Cheng explained briefly in some areas (all contributions were noted with comments)

# NOTE: Do NOT changes lines 1 to 4, *except* to fill in the "xyz" information

# Fill in with any other information required in the
#	Code Submissions Guideline (CSG).
# If there is a difference between the format above and the CSG,
#	then please use the format above.
# Copyright 2020-2022 Paul Lu
import sys
import copy     # for deepcopy()

Debug = False   # Sometimes, print for debugging.  Overridable on command line.
InputFilename = ".\\Tests\\helpdata.v1"
TargetWords = [
    'outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow',
    'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots',
    'sunny', 'windy', 'coming', 'perfect', 'need', 'sun', 'on', 'was',
    '-40', 'jackets', 'wish', 'fog', 'pretty', 'summer'
]


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


class C274:
    def __init__(self):
        self.type = str(self.__class__)
        return

    def __str__(self):
        return(self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return(s)


class ClassifyByTarget(C274):
    def __init__(self, lw=[]):
        super().__init__()      # Call superclass
        # self.type = str(self.__class__)
        self.allWords = 0
        self.theCount = 0
        self.nonTarget = []
        self.set_target_words(lw)
        self.initTF()
        return

    def initTF(self):
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        return

    # FIXME:  Incomplete.  Finish get_TF() and other getters/setters.
    def get_TF(self):
        return(self.TP, self.FP, self.TN, self.FN)

    # TODO: Could use Use Python properties
    #     https://www.python-course.eu/python3_properties.php
    def set_target_words(self, lw):
        # Could also do self.targetWords = lw.copy().  Thanks, TA Jason Cannon
        self.targetWords = copy.deepcopy(lw)
        return

    def get_target_words(self):
        return(self.targetWords)

    def get_allWords(self):
        return(self.allWords)

    def incr_allWords(self):
        self.allWords += 1
        return

    def get_theCount(self):
        return(self.theCount)

    def incr_theCount(self):
        self.theCount += 1
        return

    def get_nonTarget(self):
        return(self.nonTarget)

    def add_nonTarget(self, w):
        self.nonTarget.append(w)
        return

    def print_config(self, printSorted=True):
        print("-------- Print Config --------")
        ln = len(self.get_target_words())
        print("TargetWords (%d): " % ln, end='')
        if printSorted:
            print(sorted(self.get_target_words()))
        else:
            print(self.get_target_words())
        return

    def print_run_info(self, printSorted=True):
        print("-------- Print Run Info --------")
        print("All words:%3s. " % self.get_allWords(), end='')
        print(" Target words:%3s" % self.get_theCount())
        print("Non-Target words (%d): " % len(self.get_nonTarget()), end='')
        if printSorted:
            print(sorted(self.get_nonTarget()))
        else:
            print(self.get_nonTarget())
        return

    def print_confusion_matrix(self, targetLabel, doKey=False, tag=""):
        assert (self.TP + self.TP + self.FP + self.TN) > 0
        print(tag + "-------- Confusion Matrix --------")
        print(tag + "%10s | %13s" % ('Predict', 'Label'))
        print(tag + "-----------+----------------------")
        print(tag + "%10s | %10s %10s" % (' ', targetLabel, 'not'))
        if doKey:
            print(tag + "%10s | %10s %10s" % ('', 'TP   ', 'FP   '))
        print(tag + "%10s | %10d %10d" % (targetLabel, self.TP, self.FP))
        if doKey:
            print(tag + "%10s | %10s %10s" % ('', 'FN   ', 'TN   '))
        print(tag + "%10s | %10d %10d" % ('not', self.FN, self.TN))
        return

    def eval_training_set(self, tset, targetLabel, lines=True):
        print("-------- Evaluate Training Set --------")
        self.initTF()
        # zip is good for parallel arrays and iteration
        z = zip(tset.get_instances(), tset.get_lines())
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class()
            if lb == targetLabel:
                if cl:
                    self.TP += 1
                    outcome = "TP"
                else:
                    self.FN += 1
                    outcome = "FN"
            else:
                if cl:
                    self.FP += 1
                    outcome = "FP"
                else:
                    self.TN += 1
                    outcome = "TN"
            explain = ti.get_explain()
            # Format nice output
            if lines:
                w = ' '.join(w.split())
            else:
                w = ' '.join(ti.get_words())
                w = lb + " " + w

            # TW = testing bag of words words (kinda arbitrary)
            print("TW %s: ( %10s) %s" % (outcome, explain, w))
            if Debug:
                print("-->", ti.get_words())
        self.print_confusion_matrix(targetLabel)
        return

    def classify_by_words(self, ti, update=False, tlabel="last"):
        inClass = False
        evidence = ''
        lw = ti.get_words()
        for w in lw:
            if update:
                self.incr_allWords()
            if w in self.get_target_words():    # FIXME Write predicate
                inClass = True
                if update:
                    self.incr_theCount()
                if evidence == '':
                    evidence = w            # FIXME Use first word, but change
            elif w != '':
                if update and (w not in self.get_nonTarget()):
                    self.add_nonTarget(w)
        if evidence == '':
            evidence = '#negative'
        if update:
            ti.set_class(inClass, tlabel, evidence)
        return(inClass, evidence)

    # Could use a decorator, but not now
    def classify(self, ti, update=False, tlabel="last"):
        cl, e = self.classify_by_words(ti, update, tlabel)
        return(cl, e)

    def classify_all(self, ts, update=True, tlabel="classify_all"):
        for ti in ts.get_instances():
            cl, e = self.classify(ti, update=update, tlabel=tlabel)
        return


class TrainingInstance(C274):
    def __init__(self):
        super().__init__()              # Call superclass
        # self.type = str(self.__class__)
        self.inst = dict()
        # FIXME:  Get rid of dict, and use attributes
        self.inst["label"] = "N/A"      # Class, given by oracle
        self.inst["words"] = []         # Bag of words
        self.inst["class"] = ""         # Class, by classifier
        self.inst["explain"] = ""       # Explanation for classification
        self.inst["experiments"] = dict()   # Previous classifier runs
        self.Stop_Words = [
            "i", "me", "my", "myself", "we", "our",
            "ours", "ourselves", "you", "your",
            "yours", "yourself", "yourselves", "he",
            "him", "his", "himself", "she", "her",
            "hers", "herself", "it", "its", "itself",
            "they", "them", "their", "theirs",
            "themselves", "what", "which", "who",
            "whom", "this", "that", "these", "those",
            "am", "is", "are", "was", "were", "be",
            "been", "being", "have", "has", "had",
            "having", "do", "does", "did", "doing",
            "a", "an", "the", "and", "but", "if",
            "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with",
            "about", "against", "between", "into",
            "through", "during", "before", "after",
            "above", "below", "to", "from", "up",
            "down", "in", "out", "on", "off", "over",
            "under", "again", "further", "then",
            "once", "here", "there", "when", "where",
            "why", "how", "all", "any", "both",
            "each", "few", "more", "most", "other",
            "some", "such", "no", "nor", "not",
            "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will",
            "just", "don", "should", "now"
        ]
        self.specialchar= ["!", ".", "-", "$", "%", "'", "&",
                      "(", ")", "*", "+", ",", "/", ":", ";", "<", "=", ">", "?", "_", "[", "]", "^", "'", "{", "|", "}", "~", '@', '#']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        return

    def get_label(self):
        return(self.inst["label"])

    def get_words(self):
        return(self.inst["words"])

    def set_class(self, theClass, tlabel="last", explain=""):
        # tlabel = tag label
        self.inst["class"] = theClass
        self.inst["experiments"][tlabel] = theClass
        self.inst["explain"] = explain
        return

    def get_class_by_tag(self, tlabel):             # tlabel = tag label
        cl = self.inst["experiments"].get(tlabel)
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_explain(self):
        cl = self.inst.get("explain")
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_class(self):
        return self.inst["class"]

    def process_input_line(
        self, line, run=None,
        tlabel="read", inclLabel=False
    ):
        for w in line.split():
            if w[0] == "#":
                self.inst["label"] = w
                if inclLabel:
                    self.inst["words"].append(w)
            else:
                self.inst["words"].append(w)

        if not (run is None):
            cl, e = run.classify(self, update=True, tlabel=tlabel)
        return(self)
    
    #task1 starts here#
    def withoutstop(self,listwithstop):
        list_without_stop = []
        for stoper in listwithstop:
            if stoper not in self.Stop_Words:
                list_without_stop += [stoper]
        return(list_without_stop)
    
    def preprocess_words(self, mode=''):
        lowercased = []

        for a in self.inst["words"]:
            p = a.lower()
            lowercased.append(p)
            
        def exceptionsss(old, newlist):
            newlisted= []
            for s in newlist:
                s= list(s)
                try:
                    newvalue = int(''.join(s))
                    if newvalue < 0: 
                        s.remove("-")
                        while '' in s:
                            s.remove('')
                        newvalue = int(''.join(s))
                        newlisted += [str(newvalue)]
                    elif newvalue > 0:
                        newlisted += [str(newvalue)]
                # Heteng Mehta helped explain exceptions to me and helped a tiny amount in implementation
                except BaseException:
                    exceptified = []
                    for d in s:
                        if d not in old:
                            exceptified += [d]
                    newlisted += [(''.join(exceptified))]
            return(newlisted)
        #if condition code box
        if mode == "keep-symbols":
            edited = exceptionsss(self.numbers, lowercased)
            removedall = self.withoutstop(edited)
        elif mode == "keep-stops":
            removespecialchars = exceptionsss(self.specialchar, lowercased)
            removedigtis = exceptionsss(self.numbers, removespecialchars)
            removedall=removedigtis
        elif mode == "keep-digits":
            removespecialchars = exceptionsss(self.specialchar, lowercased)
            removedall =self.withoutstop(removespecialchars)
        else:
            removespecialchars = exceptionsss(self.specialchar, lowercased)
            removedigtis = exceptionsss(self.numbers, removespecialchars)
            removedall = self.withoutstop(removedigtis)

        while '' in removedall:
            removedall.remove('')
        
        self.inst["words"] = removedall 
        return

#Task2 starts here
class ClassifyByTopN(ClassifyByTarget):
    def target_top_n(self, tset, num=5, label=''):
        word_list = []

        for obj in tset.get_instances():

            if label == obj.get_label():
                word_list.extend(obj.get_words())

            def sort_and_analyze(word_list):
                unique_word_list = []
                for i in range(0, len(word_list)):
                    if word_list[i] not in unique_word_list:
                        unique_word_list.append(word_list[i])
                results = {}
                for i in range(0, len(unique_word_list)):
                    count = word_list.count(unique_word_list[i])
                    results[unique_word_list[i]] = count
                return results
        result_dict = sort_and_analyze(word_list)
        count_list = sorted(result_dict.values(), reverse=True)
        self.targetWords = []
        for word, freq in result_dict.items():
            if freq >= count_list[num-1]:
                self.targetWords.append(word)
        return
#Task2 ends here

class TrainingSet(C274):
    def __init__(self):
        super().__init__()      # Call superclass
        # self.type = str(self.__class__)
        self.inObjList = []     # Unparsed lines, from training set
        self.inObjHash = []     # Parsed lines, in dictionary/hash
        self.variable = dict()  # NEW: Configuration/environment variables
        return

    def set_env_variable(self, k, v):
        self.variable[k] = v
        return

    def get_env_variable(self, k):
        if k in self.variable:
            return(self.variable[k])
        else:
            return ""

    def inspect_comment(self, line):
        if len(line) > 1 and line[1] != ' ':      # Might be variable
            v = line.split(maxsplit=1)
            self.set_env_variable(v[0][1:], v[1])
        return

    def get_instances(self):
        return(self.inObjHash)      # FIXME Should protect this more

    def get_lines(self):
        return(self.inObjList)      # FIXME Should protect this more

    def print_training_set(self):
        print("-------- Print Training Set --------")
        z = zip(self.inObjHash, self.inObjList)
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class_by_tag("last")     # Not used
            explain = ti.get_explain()
            print("( %s) (%s) %s" % (lb, explain, w))
            if Debug:
                print("-->", ti.get_words())
        return

    def process_input_stream(self, inFile, run=None):
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            if len(line) == 0:   # Blank line.  Skip it.
                continue

            # Check for comments *and* environment variables
            if line[0] == '%':  # Comments must start with % and variables
                self.inspect_comment(line)
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return

    def preprocess(self, mode=''):  #task1 finished here
        for _, enumerations in enumerate(self.get_instances()):
            enumerations.preprocess_words(mode)
        return

    #Task3 starts here
    def return_nfolds(self, num=3):
        ph_list = []
        list_of_lines = []
        list_of_trainingsets = []
        countof = 0
        roundr = 0
        #discussed the creation of the structure with Ohm Panchai
        for i in range(0,num):
            ph_list.append([])
            list_of_lines.append([])
            
        for train, trl in zip(self.inObjHash, self.inObjList):
            countof = countof + 1
            roundr = (countof % num)
            if roundr == 0:
                countof= num
            ph_list[roundr-1]+= [train]
            list_of_lines[roundr - 1].append(trl)
        
        #Eric cheng explained briefly on appending to the list of trainingsets
        for o in range(0, num):
            trainsetobj = TrainingSet()
            trainsetobj.inObjHash = ph_list[o]
            trainsetobj.inObjList = list_of_lines[i]
            list_of_trainingsets.append(trainsetobj)
        return list_of_trainingsets

    def copy(self):
        # Get a deepcopy of the object
        copied = copy.deepcopy(self)
        return copied

    def add_training_set(self, tset):
        for i in range(0,len(tset.inObjHash)):
            self.inObjHash.append(copy.deepcopy(tset.inObjHash[i]))
            self.inObjList.append(copy.deepcopy(tset.inObjList[i]))
        return
#Task3 ends here

# Very basic test of functionality
def basemain():
    global Debug
    tset = TrainingSet()
    run1 = ClassifyByTarget(TargetWords)
    if Debug:
        print(run1)     # Just to show __str__
        lr = [run1]
        print(lr)       # Just to show __repr__

    argc = len(sys.argv)
    if argc == 1:   # Use stdin, or default filename
        inFile = open_file()
        assert not (inFile is None), "Assume valid file object"
        tset.process_input_stream(inFile, run1)
        inFile.close()
    else:
        for f in sys.argv[1:]:
            # Allow override of Debug from command line
            if f == "Debug":
                Debug = True
                continue
            if f == "NoDebug":
                Debug = False
                continue

            inFile = open_file(f)
            assert not (inFile is None), "Assume valid file object"
            tset.process_input_stream(inFile, run1)
            inFile.close()

    print("--------------------------------------------")
    plabel = tset.get_env_variable("pos-label")
    print("pos-label: ", plabel)
    print("NOTE: Not using any target words from the file itself")
    print("--------------------------------------------")

    if Debug:
        tset.print_training_set()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, plabel)

    return


if __name__ == "__main__":
    basemain()