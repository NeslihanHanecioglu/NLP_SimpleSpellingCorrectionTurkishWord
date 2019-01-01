# NLP_SimpleSpellingCorrectionTurkishWord
By using the METU-Sabanci Turkish Treebank (MSTT) , this python code performs a simple spelling correction in Turkish:

1. Read a word from the input, s. 
2. Retrieve all words from MSTT whose length is between |s|-1 and |s|+1 and whose first two letters are the same as the first two letters of s.
3. Calculate edit distances between s and all the words retrieved in Step 2.
4. Print the words whose edit distance is 1.
The screenshots of the program is shown in spellingCorrection_ScreenShotResult.odt
