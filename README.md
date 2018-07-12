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

## Usage

1. Clone the repository and delete content in input/ and output/ directories
2. Create and insert files/directories in the format specified above
3. Run Python program using `python main.py` in `PDF-Sorter-Combiner` directory
