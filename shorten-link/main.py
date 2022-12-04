import sys
import pyshorteners

if len(sys.argv) > 1:
    link = sys.argv[1]
else:
    link = input("Link: ")
print(pyshorteners.Shortener().tinyurl.short(link))
