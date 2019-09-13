# tagrs: a tag recommender system

Build a Baysian classifier for recommending tags for untagged 
org-mode entries.

The initial work requires developing data set that can be used for 
training and testing. The first step of this phase is parsing org-mode
files to extract headers, body and the tags for classification.

## Parsing org-mode

The [org-mode web site lists several parsers]([https://orgmode.org/worg/org-tools/index.html)
Some are written in python. They all seem somewhat dated but the format is
not complex and has been stable for some time.
