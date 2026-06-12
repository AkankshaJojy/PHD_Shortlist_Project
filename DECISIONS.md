# Design Decisions


## 1. Same name researcher collisions

Problem:

Many researchers share similar names.


Solution:

The system verifies:
- institution
- publication topics
- research areas


A researcher is only ranked when paper topics match the student's interests.



## 2. Career stage filtering

Problem:

Authors may include PhD students or postdocs.


Solution:

Profiles with missing institutions or weak publication history are removed.


## 3. Wrong domain leakage

Problem:

Keyword matching can return unrelated research.


Solution:

The system combines:
- research topics
- publication titles
- citation relevance


## 4. Country restrictions

Problem:

Students have hard country constraints.


Solution:

Country filtering happens before ranking.


## 5. Personalization

Problem:

Generic recommendations are not useful.


Solution:

An LLM generates a short explanation using:
- student interests
- researcher topics
- paper evidence