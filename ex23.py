import sys
script, encoding, error = sys.argv

def main(langauge_file,encoding,errors):
    line = langauage_file.readline()

    if line:
        print_line(line,encoding,errors)
        return main(langauage_file,encoding,errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes, "<===>",cooked_string)

langauges = open("langauges.txt", encoding="utf-8")

main(langauges, encoding, error)
