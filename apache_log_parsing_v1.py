# import re
# from collections import Counter
# import csv
# import argparse

# my_parser = argparse.ArgumentParser(description='Reading the log file')
# my_parser.add_argument("--l","--logfile",
#                        help='Please enter the logfile to parse',dest="logfile",type=argparse.FileType('r'), required=True)
# args = my_parser.parse_args()


# logreg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
# with args.logfile as f:
#     fread = f.read()
#     ip_list = re.findall(logreg, fread)
#     with open("ipnewcount.csv", "w") as f:
#         fwritercsv = csv.writer(f)
#         fwritercsv.writerow(["IP_Address", "Count"])
#         for k, v in Counter(ip_list).items():
#             fwritercsv.writerow([k, v])


#Version_2
# import re
# from collections import Counter
# import csv
# import argparse


# logreg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# # Create the parser
# my_parser = argparse.ArgumentParser(description='Reading the log and csv file')
# my_parser.add_argument("--l","--logfile",
#                        help='Please enter the logfile to parse',dest="logfile",type=argparse.FileType('r'), required=True)
# args = my_parser.parse_args()


# def read_file(logfile):
#     with args.logfile as f:
#         log = f.read()
#         ip_list = re.findall(logreg,log)
#         return ip_list

# def read_count():
#     ip_list = read_file(args.logfile)
#     ip_count = Counter(ip_list)
#     return ip_count.items()


# def csv_write():
#     counter = read_count()
#     with open("ip_count.csv",'w') as f:
#         fwriter = csv.writer(f)

#         fwriter.writerow(["IP_Address","Count"])
#         for item,val in counter:
#             fwriter.writerow([item, val])

# if __name__ == '__main__':
#     csv_write()


# Version_3
# import re
# import csv
# import argparse
# from collections import Counter

# IP_REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# # Create the parser
# parser = argparse.ArgumentParser(description='Reading the log and CSV file')
# parser.add_argument("--l", "--logfile",
#                     help='Please enter the logfile to parse',
#                     dest="logfile",
#                     type=argparse.FileType('r'),
#                     required=True)

# def extract_ips(logfile):
#     """Extracts all IP addresses from the given logfile."""
#     try:
#         with open(logfile, 'r') as f:
#             log = f.read()
#     except Exception as e:
#         print(f"Error reading file: {e}")
#         return []
#     return re.findall(IP_REGEX, log)

# def count_ips(ip_list):
#     """Count the occurrence of each IP address in the list."""
#     return Counter(ip_list)

# def write_csv(counter):
#     """Write the counter data to a CSV file."""
#     try:
#         with open("ip_count.csv", 'w') as f:
#             writer = csv.DictWriter(f, fieldnames=["IP_Address", "Count"])
#             writer.writeheader()
#             for item, count in counter.items():
#                 writer.writerow({"IP_Address": item, "Count": count})
#     except Exception as e:
#         print(f"Error writing CSV file: {e}")

# def main():
#     args = parser.parse_args()
#     ip_list = extract_ips(args.logfile)
#     ip_counter = count_ips(ip_list)
#     write_csv(ip_counter)

# if __name__ == '__main__':
#     main()


#Version_4
# import re
# import csv
# import argparse
# from collections import Counter

# IP_REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# # Create the parser
# parser = argparse.ArgumentParser(description='Parse a log file and output IP address occurrences to a CSV file.')
# parser.add_argument("--l", "--logfile",
#                     help='Logfile to parse',
#                     dest="logfile",
#                     type=argparse.FileType('r'),
#                     required=True)
# parser.add_argument("--o", "--output",
#                     help='Output CSV file name',
#                     dest="outputfile",
#                     type=str,
#                     default="ip_count.csv")

# def extract_ips(logfile):
#     """Extracts all IP addresses from the given logfile."""
#     return re.findall(IP_REGEX, logfile.read())

# def count_ips(ip_list):
#     """Count the occurrence of each IP address in the list."""
#     return Counter(ip_list)

# def write_csv(counter, filename):
#     """Write the counter data to a CSV file."""
#     with open(filename, 'w', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=["IP_Address", "Count"])
#         writer.writeheader()
#         for item, count in counter.items():
#             writer.writerow({"IP_Address": item, "Count": count})
#     print(f"IP counts written to {filename}")

# def main():
#     args = parser.parse_args()
#     ip_list = extract_ips(args.logfile)
#     ip_counter = count_ips(ip_list)
#     write_csv(ip_counter, args.outputfile)

# if __name__ == '__main__':
#     main()
