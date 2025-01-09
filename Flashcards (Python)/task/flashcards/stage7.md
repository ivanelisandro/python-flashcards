# Stage 7:

For stage 7 we should add command line arguments for the script.


**Objectives:**

When provided with command-line arguments, your program should do the following:

- If `--import_from=IMPORT` is passed, where `IMPORT` is the file name, read the initial card set from the external file, and print the message `n cards have been loaded.` as the first line of the output, where `n` is the number of cards loaded from the external file. If such an argument is not provided, the set of cards should initially be empty and no message about card loading should be output.
- If `--export_to=EXPORT` is passed, where `EXPORT` is the file name, write all cards that are in the program memory into this file after the user has entered `exit`, and the last line of the output should be `n cards have been saved.`, where `n` is the number of flashcards in the set.


## Run arguments examples

```
python flashcards.py --import_from=derivatives.txt
```

```
python flashcards.py --export_to=animals.txt
```

```
python flashcards.py --import_from=words13june.txt --export_to=words14june.txt
```

```
python flashcards.py --export_to=vocab.txt --import_from=vocab.txt
```
