# Collection of Programming Challenges for AnkiCode

## Decks
  Decks src code is located in the `src` folder
  Compiled decks are located in the `dist` folder in .csv format

## Build decks
  Build decks with the following command:
  `python3 build_decks.py`
  As the result, csv files will be generated and placed into `dist` folder
  
## Add new coding problems to the existing deck
   - `title/<problem_name>` - contains a title of a new coding problem
   - `description/<problem_name>` - contains a text description of a new coding problem
   - `fn_names/<problem_name>` - function name which will be used in the solution template
   - `solutions/cpp/<problem_name>` - markdown file containing C++ solution of a problem
   - `solutions/python/<problem_name>` - markdown file containing Python solution of a problem
   - `solutions/java/<problem_name>` - markdown file containing Java solution of a problem
   - `solutions/js/<problem_name>` - markdown file containing JavaScript solution of a problem
   - `test_cases/<problem_name>` - a TSV (tab-separated) file with test-cases

## Add a new deck
   To add a new deck - simply copy the `template` folder

