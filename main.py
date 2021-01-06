#!/bin/python3
import sys

verbose = False

if len(sys.argv) > 2:
    print("Usage: python3 main.py [-v] < input > output")
    sys.exit()
elif len(sys.argv) == 2 and sys.argv[1] in ["-v", "--verbose"]:
    verbose = True
elif len(sys.argv) == 2:
    print("Usage: python3 main.py [-v] < input > output")
    sys.exit()

# Constants
METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Helper Functions
is_method = lambda x: x.upper() in METHODS
is_route = lambda x: x.startswith("/")
is_parameter = lambda x: x.startswith("?") and x.count("=") == x.count("&")+1
is_json = lambda x: x.lower() == "json"
is_json_start = lambda x: x.startswith("json[")
is_json_complete = lambda x: x.count('[') - x.count('\\[') == x.count(']') - x.count('\\]') and x.count('{') - x.count('\\{') == x.count('}') - x.count('\\}') and x.count('<') - x.count('\\<') == x.count('>') - x.count('\\>') and x.count('(') - x.count('\\(') == x.count(')') - x.count('\\)') # Check if there are the same amounts of each pair of symbols for open and close, minus the escaped ones.
is_split = lambda x: x == "|"
is_same_split = lambda x: x == "^"
is_response = lambda x: x == "->"
is_http_code = lambda x: x.isdigit() and x[0] in ['1','2','3','4','5'] and len(x) == 3
is_reason = lambda x: x.count('"') == 2 and x.startswith('"') and x.endswith('"')
is_reason_start = lambda x: x.count('"') == 1 and x.startswith('"')
is_reason_complete = lambda x: x.count('"') == 2 and x.endswith('"')
is_name = lambda x: x.startswith("{") and x.endswith("}")
is_name_start = lambda x: x.startswith("{")
is_name_complete = lambda x: x.endswith("}") # This means you can embed {} inside the name, except right before a space.

try:
    while True:
        i = input()
        if i.startswith('#'):
            if i.startswith('####'):
                print('###' + i[4:])
                if verbose:
                    print('HEADING 3', file=sys.stderr)
            elif i.startswith('###'):
                print('##' + i[3:])
                if verbose:
                    print('HEADING 2', file=sys.stderr)
            elif i.startswith('##'):
                print('#' + i[2:])
                if verbose:
                    print('HEADING 1', file=sys.stderr)
            elif verbose:
                print('COMMENT', file=sys.stderr)
            continue
        raw_chunks = i.split()
        chunks = []
        heap = ""
        structure = []
        json = False
        prev_is_http_code = False
        reason = False
        name = False
        for raw_chunk in raw_chunks:
            if json:
                heap += raw_chunk
                if is_json_complete(heap):
                    chunks.append(heap)
                    heap = ""
                    json = False
                    structure.append("JSON_C")
            elif reason:
                heap += raw_chunk
                if is_reason_complete(heap):
                    chunks.append(heap.replace("+", " "))
                    heap = ""
                    reason = False
                    structure.append("REASON_L")
            elif name:
                heap += raw_chunk
                if is_name_complete(heap):
                    chunks.append(heap)
                    heap = ""
                    name = False
                    structure.append("NAME_L")
            elif prev_is_http_code:
                chunks.append(raw_chunk)
                structure.append("HTTP_TEXT")
                prev_is_http_code = False
            elif is_method(raw_chunk):
                chunks.append(raw_chunk.upper())
                structure.append("METHOD") 
            elif is_route(raw_chunk):
                chunks.append(raw_chunk)
                structure.append("ROUTE")
            elif is_parameter(raw_chunk):
                chunks.append(raw_chunk)
                structure.append("PARAMETER")
            elif is_json(raw_chunk):
                chunks.append(raw_chunk.lower())
                structure.append("JSON")
            elif is_json_start(raw_chunk):
                json = True
                heap += raw_chunk
            elif is_split(raw_chunk):
                chunks.append(raw_chunk)
                structure.append("SPLIT")
            elif is_same_split(raw_chunk):
                chunks.append(raw_chunk)
                structure.append("SAMESPLIT")
            elif is_response(raw_chunk):
                chunks.append(raw_chunk)
                structure.append("RESPONSE")
            elif is_http_code(raw_chunk):
                chunks.append(raw_chunk)
                structure.append("HTTP_CODE")
                prev_is_http_code = True
            elif is_reason(raw_chunk):
                chunks.append(raw_chunk)
                structure.append("REASON")
            elif is_reason_start(raw_chunk):
                heap += raw_chunk
                reason = True
            elif is_name(raw_chunk):
                chunks.append(raw_chunk)
                structure.append("NAME")
            elif is_name_start(raw_chunk):
                heap += raw_chunk
                name = True
            else:
                chunks.append(raw_chunk)
                structure.append("UNKNOWN")
        if verbose:
            print(" ".join(structure), file=sys.stderr)
        indent = 0
        for index in range(len(structure)):
            if structure[index] == "UNKNOWN":
                raise SyntaxError("Bad syntax")
        print(" ".join(chunks))
except EOFError:
    sys.exit()
except KeyboardInterrupt:
    print("Interrupted", file=sys.stderr)
except Exception as e:
    print("Unexpected error %s:" % type(e).__name__, e, file=sys.stderr)
