#
#  Copyright (C) 2003  greg Landrum and Rational Discovery LLC
#

""" """
import RDConfig
import unittest
from ML.DecTree import ID3,PruneTree,CrossValidate
import copy
import cPickle

def feq(a,b,tol=1e-4):
  return abs(a-b)<=tol

class TreeTestCase(unittest.TestCase):
  def setUp(self):
    pass
    
  def test1(self):
    " testing pruning with known results "
    oPts= [ \
      [0,0,1,0],
      [0,1,1,1],
      [1,0,1,1],
      [1,1,0,0],
      [1,1,1,1],
      ]
    tPts = oPts+[[0,1,1,0],[0,1,1,0]]
    tree = ID3.ID3Boot(oPts,attrs=range(3),nPossibleVals=[2]*4)
    err,badEx = CrossValidate.CrossValidate(tree,oPts)
    assert err==0.0,'bad initial error'
    assert len(badEx)==0,'bad initial error'

    # prune with original data, shouldn't do anything
    newTree,err = PruneTree.PruneTree(tree,[],oPts)
    assert newTree==tree,'improper pruning'
    
    # prune with train data
    newTree,err = PruneTree.PruneTree(tree,[],tPts)
    assert newTree!=tree,'bad pruning'
    assert feq(err,0.14286),'bad error result'
    
if __name__ == '__main__':
  unittest.main()
  
  