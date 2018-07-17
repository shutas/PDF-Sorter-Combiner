# PDF-Sorter-Combiner

Written by Shuta Suzuki (shutas@umich.edu)

Retrieves HTML source code using the specified links and creates a list of PDF filenames in the order they appear on the webpage. Rearranges the PDF files in the local directory by the same order and merges them into one PDF file. Outputs error reports if merge fails due to inconsistencies.

## Prerequisites

The file directory should be set up in this format:  
(Files in parenthesis will be generated after running the program)

```
PDF-Sorter-Combiner/
├── config.py
├── input/
│   ├── university_list.csv
│   ├── A大学_2017/
│   │   ├── one.pdf
│   │   ├── two.pdf
│   │   └── three.pdf
│   └── B大学_2016/
│       ├── four.pdf
│       ├── five.pdf
│       └── six.pdf
├── main.py
└── output/
    ├── (combined1.pdf)
    ├── (combined2.pdf)
    └── (error_report_2015.txt)
```

Note that ALL of the PDF files you want to merge together must be provided beforehand under the same directory. The naming convention for the directories should be `<University Name>_<Year>/`. All of the PDF files should NOT be renamed, as this program depends on the files to have the original names (i.e. the same name embedded in the specified HTML source code).

## File Format

`university_list.csv` should have two columns with labels `大学名` and `URL`. `大学名` should have the name of universities, and `URL` should have the URL links to the webpage of the respective university that include the download links to all the documents which you want to merge.

## Usage

1. Clone the repository and delete content in `input` and `output` directories
2. Create and insert files/directories in the format specified above
3. Run Python program using `python main.py` in `PDF-Sorter-Combiner` directory
4. Adjust confuguration variables as necessary in `config.py`
