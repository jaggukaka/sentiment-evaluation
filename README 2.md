sentiment-evaluation
====================

A tool for evaluating the accuracy of Sentiment Analysis REST API services, against a gold standard dataset (a list of manually annotated sentences). Currently supports: [AIApplied](https://ai-applied.squarespace.com/), [Alchemy](http://www.alchemyapi.com/), [Bitext](http://www.bitext.com/bitext-api-2.html), [Chatterbox](http://chatterbox.co/), [Datumbox](http://www.datumbox.com/machine-learning-api/), [Lymbix](http://www.lymbix.com/), [Repustate](https://www.repustate.com/), [Semantria](https://semantria.com/), [Sentigem](http://sentigem.com/), [Skyttle](http://www.skyttle.com/), and [Viralheat](https://app.viralheat.com/developer).

**Installation**

1. Install requirements:

    ``pip install -r requirements.txt``

    ``pip install -r requirements-testing.txt`` (optionally, for testing the code)

2. The gold standard data should be a text file, where on each line there is a document (with tabs and newline removed) followed by a tab character, followed by the manually assigned label: "0" for neutral, "+" for positive, "-" for negative, "X" for irrelevant (these documents will be excluded from the evaluation). See example in ``evaluation_data.txt``.

3. Obtain access keys for each API you’d like to evaluate, and put them into ``config.txt`` found in the root folder.

4. Optionally, comment out APIs that should not be included into the comparison in ``compare.py``, ``ANALYZERS_TO_USE``.

**Usage**

    ``python compare.py path-to-text-file-with-annotated-data path-to-config-file``

**Output**

*results.csv*: a table where against each document of the gold standard data, there are labels output by each analyzer.

Accuracy and error rates for each analyzer are printed to stdout.

*Accuracy rate* is the proportion of correctly assigned labels to the total number of documents in the gold standard. Ranges between 0.0 and 1.0.

*Error rate* is calculated taking into account whether a neutral label was confused with a positive or negative one (the error has the weight of 1), or a positive label was confused with a negative one (the error has the weight of 2). Error rate is the proportion of the sum of observed weighted errors to the maximum possible sum of weighted errors. Ranges between 0.0 and 1.0.

More information can be found [here](http://blog.skyttle.com/?p=100).

**Notes**

* The API providers impose limits on the free usage of the APIs, so if you don't want to incur charges, make sure the size of your test data is within the free usage allowance for all analyzers that you include into the comparison.

* [Semantapi](http://www.semantapi.com/) is a similar project, written in C#.

