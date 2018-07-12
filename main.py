"""Script to Automate PDF Combination."""

import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader, PdfFileMerger
import config

def create_university_dictionary():
    """Create university dictionary used when crawling websites."""
    # Open URL file
    university_list_file_obj = open(config.UNIVERSITY_LIST_FILEPATH, "r")

    # Process URL list
    while True:
        
        # Read a line
        line = university_list_file_obj.readline()

        # Content in line; Add entry to dict
        if line:
            (university_name, university_url) = line.split(",")

            # Skip header
            if university_name != "大学名":
                config.UNIVERSITY_DICT[university_name] = university_url
        
        # Reached end of file; Quit reading
        else:
            break

    # Close URL file
    university_list_file_obj.close()


def combine_pdf():
    """Combine PDF files if conditions are met."""
    # Iterate for each university
    for university, link in config.UNIVERSITY_DICT.items():
        
        # Initialize data structures for each university
        pdf_filename_list = []

        # Get source code of link
        source_code_str = urlopen(link)

        # Create HTML parser
        soup = BeautifulSoup(source_code_str, "html.parser")

        # Create a list of PDF documents in order
        for a_tag in soup.find_all("a"):
            
            # Sanitize filename by removing directory names
            href_value = a_tag.get("href").split("/")[-1]

            # If PDF file is found, add it to list
            if ".pdf" in href_value:
                pdf_filename_list.append(href_value)

        # Open current university's relevant folder
        university_dirname = university + "_" + config.YEAR
        university_full_dirname = os.path.join(config.INPUT_DIR_PATH,
                                               university_dirname)

        # Ordered list for PDFs to combine
        ordered_pdf_filename_list = []

        # Check files in pdf_filename_list; Insert to ordered list if present
        for filename in pdf_filename_list:
            new_filepath = os.path.join(university_full_dirname, filename)
            if os.path.exists(new_filepath):
                ordered_pdf_filename_list.append(new_filepath)

        # Check if all files are appended to ordered list
        original_file_list = [item for item in 
                              os.listdir(university_full_dirname)]
        
        # If none are missing, combine PDFs
        if len(ordered_pdf_filename_list) == len(original_file_list):

            # Create list of PDF readers
            pdf_reader_list = []
            
            for filename in ordered_pdf_filename_list:
                pdf_reader = PdfFileReader(open(filename, "rb"))
                pdf_reader_list.append(pdf_reader)

            # Initialize PDF merger
            pdf_merger = PdfFileMerger()

            # Feed PDF readers to PDF merger
            for r in pdf_reader_list:
                pdf_merger.append(r)

            # Output merged PDF file
            merged_pdf_filename = university + ".pdf"
            pdf_merger.write(os.path.join(config.OUTPUT_DIR_PATH,
                                          merged_pdf_filename))
        
        # If some are missing, write to error report
        else:
            error_report_filename = "error_report_" + config.YEAR + ".txt"
            error_report_filepath = os.path.join(config.OUTPUT_DIR_PATH,
                                                 error_report_filename)

            # Update error report
            error_report_file_obj = open(error_report_filepath, "a+")
            error_report_file_obj.write(university + "\n")
            error_report_file_obj.close()


def main():
    """Driver program for PDF combiner."""
    # Initialize University Dictionary
    create_university_dictionary()

    # Start Creating Combined PDFs
    combine_pdf()

if __name__ == "__main__":
    main()