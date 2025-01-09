# Python project: Flashcards

This is one of the projects provided by JetBrains Academy, a platform for studying programming languages.
I particularly used it to start learning python while using the PyCharm IDE for their great integration with the service.

This project consists of a command line application that allows the user to:

- add study cards consisting of "term" and "definition";
- study with created cards by being asked to answer the "definition" for a random "term" between the created cards;
- export created cards to a file;
- import cards from a file (pre-created cards will be kept in the running application and exiting cards will have their definitions updated);
- check the card(s) with the most mistakes after studying;
- reset mistakes statistics whenever necessary;

## Command line arguments

If you don't want to export or import files manually you can specify command line arguments when running the script:

- Use `--import_from=some_file_name` to specify a file to automatically import cards when starting the script;
- Use `--export_to=some_file_name` to specify a file to automatically export cards when using the exit command to finish the script;

The arguments can be used individually or together and the order of the arguments is not important.

### Examples:

```
python flashcards.py --import_from=cardsimport.txt --export_to=cardsexport.txt
```

```
python flashcards.py --export_to=cards.json --import_from=cards.json
```