#!/usr/bin/env python3
# The line above is known as a "shebang", a shortened version of "hash bang".
# Hash refers to the # character, and bang refers to the ! character.

import sys
import argparse
import math

def main():
    # argparse is generally a good idea to use, because it handles edge cases.
    parser = argparse.ArgumentParser(description="Calculate the percentage of HTTP responses in each of the 1xx, 2xx, 3xx, 4xx, and 5xx ranges.")
    parser.add_argument("input_file", type=str, help="The file to process.")

    args = parser.parse_args()

    # This is encapsulated in a function
    # so that others can import our script as a library if they want.
    calculate_percentages(args.input_file)

def calculate_percentages(input_file):
    # We're going to use a neat trick to store counts of status code ranges in this.
    # We will truncate the status code to the hundreds, and then divide by 100.
    # So 2xx will go in counts[2], 3xx in counts[3], etc.
    counts = [0, 0, 0, 0, 0, 0]

    with open(input_file, "r") as f:
        for line in f:
            try:
                # Try to retrieve the status code from the line.
                ret_code = parse_line(line)

                # math.trunc cuts off the number to an integer
                # So we divide by 100 to put the last 2 number behind the decimal
                # and then truncate to remove them.
                ret_category = math.trunc(int(ret_code)/100)

                # We can use the ret_category as an index for our counts list.
                counts[ret_category] += 1
            except IndexError:
                # The line is not long enough to be valid, discard it.
                continue

    # Below is a debugging section.  You can uncomment it to get counts for individual status code ranges.
    # print("2xx: " + str(counts[2])) # These are successful
    # print("3xx: " + str(counts[3])) # These are successful
    # print("4xx: " + str(counts[4])) # These are client errors, but our service as okay, so they are successful
    # print("5xx: " + str(counts[5])) # We will count these as errors

    # Anything in the 2xx, 3xx, or 4xx range is considered successful
    successfulResponses = counts[2] + counts[3] + counts[4]

    # Add in the 5xx range, and that is the total
    totalResponses = successfulResponses + counts[5]

    successfulPercent = float(successfulResponses*100)/float(totalResponses)

    print("{}% successful requests".format(successfulPercent))



def parse_line(line):
    # Split the line into an array on spaces
    parts = line.split(" ")

    # If you count elements by spaces, the return code is the 9th element.
    # This will throw an exception if the list is too short, but we can't
    # handle that here, so we let it throw the exception.
    return parts[8]

# If this is called as a script, instead of imported as a library, run the "main" function.
if __name__ == "__main__":
    main()