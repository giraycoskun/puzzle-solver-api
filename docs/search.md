# Search Based Solutions

## AIMA4e  

__function__ UNIFORM-COST-SEARCH(_problem_) __returns__ a solution, or failure  
&emsp;__if__ problem's initial state is a goal __then return__ empty path to initial state  
&emsp;_frontier_ &larr; a priority queue ordered by pathCost, with a node for the initial state  
&emsp;_reached_ &larr; a table of {_state_: the best path that reached _state_}; initially empty  
&emsp;_solution_ &larr; failure  
&emsp;__while__  _frontier_ is not empty __and__ top(_frontier_) is cheaper than _solution_ __do__  
&emsp;&emsp;&emsp;_parent_ &larr; pop(_frontier_)  
&emsp;&emsp;&emsp;__for__ _child_ __in__ successors(_parent_) __do__   
&emsp;&emsp;&emsp;&emsp;&emsp;_s_ &larr; _child_.state  
&emsp;&emsp;&emsp;&emsp;&emsp;__if__ _s_ is not in _reached_  __or__ _child_ is a cheaper path than _reached_[_s_] __then__  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_reached_[_s_] &larr; _child_  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;add _child_ to the _frontier_  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;__if__ _child_ is a goal and is cheaper than _solution_ __then__  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_solution_  =  _child_  
&emsp;__return__ _solution_

---
__Figure 3.11__ Uniform-cost search on a graph. Finds optimal paths for problems with varying step costs. __From__ <http://aima.cs.berkeley.edu/global-index.html>

::: solvers.search.ucs.UniformCostSearch
