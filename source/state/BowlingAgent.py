from .. import constants as c
from ..state import level
from ..component import menubar
import sys
import inspect
import heapq
import random
import io
import functools
import numpy

class bowling_agent():
    def __init__(self):
        self.qvalue = Counter()
        self.eps = 0.15 #探索率
        self.gamma = 0.8 #衰减率
        self.alpha = 0.4 #学习率
        self.qvalue = Counter()
    
    def get_qvalue(self, state:tuple, action:tuple): #状态 包含：坚果数，爆炸数，每个格子的僵尸血量
        if state not in self.qvalue.keys():
            # print(len(self.qvalue))
            self.qvalue[state] = Counter()
        return self.qvalue[state][action]
    
    def get_value_from_qvalue(self, state: tuple):
        actions = self.get_legal_actions(state)
        if len(actions) == 0:
            return 0.0
        return max([self.get_qvalue(state, action) for action in actions])
    
    def compute_action_from_q(self, state):
        actions = self.get_legal_actions(state)
        if len(actions) == 0:
            return None
        for action in actions:
            self.get_qvalue(state, action)
        return self.qvalue[state].argMax()
    
    def get_action(self, state):
        actions = self.get_legal_actions(state)
        action = None
        if not len(actions) == 0:
            r = random.random()
            if r < self.eps:  random_choose = 1
            else: random_choose = 0
            if random_choose:
                #add:随机采取动作时，加入None
                actions.append(None)
                action = random.choice(actions)
            else:
                action = self.compute_action_from_q(state)
                if action != None:
                    print(action) 
        return action
        
        
    def update(self, state:tuple, action:tuple, next_state:tuple, reward:float):

        current_q = self.get_qvalue(state, action)
        self.qvalue[state][action] = (1 - self.alpha) * current_q + self.alpha * (reward + self.gamma * self.get_value_from_qvalue(next_state))
        #print(self.qvalue[state])
    
    #add: 获取合法动作
    def get_legal_actions(self, state:tuple)->list:
        actions = []
        #fix:取消直接定义的null action
        actions.append(None)
        for x in range(3):
            for y in range(5):
                if state[0]:
                    actions.append((x, y, 0))
                if state[1]:
                    actions.append((x, y, 1))
        return actions
    
""" class ApproximateBowlingAgent(bowling_agent):
    def __init__(): """
        
        
#说明：引用自hw5       
class Counter(dict):
    """
    A counter keeps track of counts for a set of keys.

    The counter class is an extension of the standard python
    dictionary type.  It is specialized to have number values
    (integers or floats), and includes a handful of additional
    functions to ease the task of counting data.  In particular,
    all keys are defaulted to have value 0.  Using a dictionary:

    a = {}
    print a['test']

    would give an error, while the Counter class analogue:

    >>> a = Counter()
    >>> print a['test']
    0

    returns the default 0 value. Note that to reference a key
    that you know is contained in the counter,
    you can still use the dictionary syntax:

    >>> a = Counter()
    >>> a['test'] = 2
    >>> print a['test']
    2

    This is very useful for counting things without initializing their counts,
    see for example:

    >>> a['blah'] += 1
    >>> print a['blah']
    1

    The counter also includes additional functionality useful in implementing
    the classifiers for this assignment.  Two counters can be added,
    subtracted or multiplied together.  See below for details.  They can
    also be normalized and their total count and arg max can be extracted.
    """

    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)

    def incrementAll(self, keys, count):
        """
        Increments all elements of keys by the same count.

        >>> a = Counter()
        >>> a.incrementAll(['one','two', 'three'], 1)
        >>> a['one']
        1
        >>> a['two']
        1
        """
        for key in keys:
            self[key] += count

    def argMax(self):
        """
        Returns the key with the highest value.
        """
        if len(list(self.keys())) == 0:
            return None
        all = list(self.items())
        values = [x[1] for x in all]
        maxIndex = values.index(max(values))
        return all[maxIndex][0]

    def sortedKeys(self):
        """
        Returns a list of keys sorted by their values.  Keys
        with the highest values will appear first.

        >>> a = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> a['third'] = 1
        >>> a.sortedKeys()
        ['second', 'third', 'first']
        """
        sortedItems = list(self.items())

        def compare(x, y): return sign(y[1] - x[1])
        sortedItems.sort(key=functools.cmp_to_key(compare))
        return [x[0] for x in sortedItems]

    def totalCount(self):
        """
        Returns the sum of counts for all keys.
        """
        return sum(self.values())

    def normalize(self):
        """
        Edits the counter such that the total count of all
        keys sums to 1.  The ratio of counts for all keys
        will remain the same. Note that normalizing an empty
        Counter will result in an error.
        """
        total = float(self.totalCount())
        if total == 0:
            return
        for key in list(self.keys()):
            self[key] = self[key] / total

    def divideAll(self, divisor):
        """
        Divides all counts by divisor
        """
        divisor = float(divisor)
        for key in self:
            self[key] /= divisor

    def copy(self):
        """
        Returns a copy of the counter
        """
        return Counter(dict.copy(self))

    def __mul__(self, y):
        """
        Multiplying two counters gives the dot product of their vectors where
        each unique label is a vector element.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['second'] = 5
        >>> a['third'] = 1.5
        >>> a['fourth'] = 2.5
        >>> a * b
        14
        """
        sum = 0
        x = self
        if len(x) > len(y):
            x, y = y, x
        for key in x:
            if key not in y:
                continue
            sum += x[key] * y[key]
        return sum

    def __radd__(self, y):
        """
        Adding another counter to a counter increments the current counter
        by the values stored in the second counter.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['third'] = 1
        >>> a += b
        >>> a['first']
        1
        """
        for key, value in list(y.items()):
            self[key] += value

    def __add__(self, y):
        """
        Adding two counters gives a counter with the union of all keys and
        counts of the second added to counts of the first.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['third'] = 1
        >>> (a + b)['first']
        1
        """
        addend = Counter()
        for key in self:
            if key in y:
                addend[key] = self[key] + y[key]
            else:
                addend[key] = self[key]
        for key in y:
            if key in self:
                continue
            addend[key] = y[key]
        return addend

    def __sub__(self, y):
        """
        Subtracting a counter from another gives a counter with the union of all keys and
        counts of the second subtracted from counts of the first.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['third'] = 1
        >>> (a - b)['first']
        -5
        """
        addend = Counter()
        for key in self:
            if key in y:
                addend[key] = self[key] - y[key]
            else:
                addend[key] = self[key]
        for key in y:
            if key in self:
                continue
            addend[key] = -1 * y[key]
        return addend

def sign(x):
    """
    Returns 1 or -1 depending on the sign of x
    """
    if(x >= 0):
        return 1
    else:
        return -1