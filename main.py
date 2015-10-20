__autor__ = "vah13"
import requests

word_list = ["Abend", "Absolute", "address", "Coding", "Access", "violation", "ACM", "Action", "statement",
             "ActionScript", "ActiveX", "Ada", "Advanced", "SCSI", "Programming", "Interface", "Aggregation", "Agile",
             "development", "methods", "Manifesto", "Alert", "Algol", "Algorithm", "Ambient", "Occlusion", "AOP", "API",
             "Applet", "Argument", "Arithmetic", "operator", "Array", "of", "pointers", "ASCII", "ASPI", "Assembler",
             "Assembly", "Associative", "operation", "AutoHotkey", "Automata-based", "Automated", "unit", "testing",
             "B", "Babel", "Backend", "Back-face", "culling", "Background", "thread", "Backpropagation", "neural",
             "network", "Base", "Batch", "file", "job", "BCPL", "Bean", "BeanShell", "Binary", "Search", "Bind", "Bit",
             "shift", "Bitwise", "operators", "Block", "BOM", "Bool", "Boolean", "Bracket", "Branch", "Brooks", "Bug",
             "tracking", "Bugfairy", "Build", "computer", "Bytecode", "C", "sharp", "C++", "C#", "Camel", "book",
             "CamelCase", "Captured", "variable", "CC", "Chaos", "model", "Char", "Character", "code", "encoding",
             "set", "Circuit", "satisfiability", "problem", "Class", "Classpath", "Clojure", "Closure", "CLR", "COBOL",
             "Cocoa", "touch", "refactoring", "Codepage", "CoffeeScript", "Command", "language", "Comment", "Common",
             "business", "oriented", "Gateway", "Compilation", "Compile", "Compiler", "Complementarity", "Compute",
             "science", "Commutative", "Concat", "Concatenation", "Concurrency", "Conditional", "expression",
             "Constructor", "chaining", "Content", "migration", "Control", "flow", "CPAN", "CPL", "Crapplet", "CSAT",
             "CSS", "compressor", "editor", "Curly", "Curry", "CVS", "D", "DarkBASIC", "Dataflow", "Data-flow",
             "analysis", "Data", "diagram", "source", "type", "Datalog", "DDE", "Dead", "Debug", "Debugger",
             "Debugging", "Declaration", "Declarative", "Declare", "Decompiler", "Deductive", "database", "Dense",
             "matrix", "Dereference", "Dependent", "Developer", "DHTML", "Die", "Diff", "Direct", "Discrete",
             "optimization", "Dissembler", "Django", "DML", "Do", "DOM", "Dragon", "Dribbleware", "Dump", "Dylan",
             "Dynamic", "E", "Eclipse", "ECMAScript", "Eight", "queens", "Element", "Ellipsis", "Else", "if", "Elsif",
             "Embedded", "Java", "Encapsulation", "Endian", "Endless", "loop", "EOF", "Epoch", "Eq", "Error",
             "Errorlevel", "Esac", "Escape", "sequence", "Eval", "Event", "handler", "listener", "Event-driven", "Exec",
             "Exception", "handling", "Exists", "Exponential", "backoff", "F", "F#", "False", "Fifth", "generation",
             "First", "First-class", "object", "Flag", "Flat", "Floating-point", "For", "Foreach", "Forth", "FORTRAN",
             "Framework", "Front", "end", "Function", "Functional", "G", "Game", "Life", "Gang", "four", "Garbage",
             "collection", "Gaussian", "pyramid", "GCC", "Ge", "General-purpose", "Genetic", "GIGO", "Glitch", "Glue",
             "Go", "Goto", "GPL", "GT", "GTK", "GW", "BASIC", "H", "HAL", "Hard", "Hash", "Haskell", "Heap", "Hello",
             "world", "Heuristic", "evaluation", "Hex", "HDML", "Hiew", "High-level", "HTML", "form", "head",
             "Hungarian", "notation", "Hwclock", "Hypertext", "Markup", "I", "IDE", "Immutable", "Imperative",
             "Implicit", "parallelism", "Indirection", "Inherent", "Inheritance", "Inline", "Input/output", "Instance",
             "Instantiation", "Instructions", "Int", "Integer", "Integrated", "Environment", "IntelliJ", "IDEA",
             "Intermediate", "Interpreted", "Interpreter", "Invalid", "IPC", "ISAPI", "Iteration", "J", "champion",
             "EE", "ME", "native", "reserved", "words", "JavaBean", "Javac", "JavaFX", "JavaScript", "JavaScriptCore",
             "Javax", "JBuilder", "JCL", "JDBC", "JDK", "JIL", "JIT", "JHTML", "JNI", "JRE", "JScript", "JSON", "JSP",
             "JSR", "JVM", "K", "Karel", "Kit", "Kludge", "Kluge", "L", "Label", "Lambda", "calculus", "processor",
             "Lexical", "Lexicon", "Linker", "LISP", "Live", "script", "Literal", "LLVM", "Local", "optimum", "Logic",
             "Logical", "LOGO", "Lookup", "table", "Loony", "bin", "Loophole", "Loosely", "typed", "Low-level",
             "Library", "LT", "Lua", "LUT", "M", "Machine", "Magic", "quotes", "Map", "Math", "Matlab", "Mbean",
             "Memorization", "Mercurial", "Meta-character", "Metaclass", "Metalanguage", "Method", "overloading",
             "Middleware", "Module", "Monte", "Carlo", "MSDN", "MSVC", "Multi-pass", "MUMPS", "Mutex", "N", "NaN", "Ne",
             ".NET", "Natural", "NBSP", "NDA", "Nested", "join", "Newline", "Nil", "pointer", "Node.js", "Nodelist",
             "Noncontinuous", "structure", "Non-Disclosure", "Agreement", "Nonadjustable", "NO-OPeration", "Null", "O",
             "Object-oriented", "Objective-C", "Obfuscated", "OCaml", "Octave", "ODBC", "OOP", "One-pass", "Open",
             "Connectivity", "OpenGL", "polygon", "Operand", "associatively", "precedence", "OR", "Overflow",
             "Overload", "P", "P-code", "Package", "Parenthesis", "Parse", "Pascal", "case", "Pastebin", "PDL", "Perl",
             "Persistent", "memory", "PersonalJava", "PHP", "Phrase", "tag", "Pick", "Pickling", "PicoJava", "Pipe",
             "Pixel", "shader", "POD", "Polymorphism", "Pop", "Private", "Procedural", "Procedure", "Process",
             "Program", "generator", "listing", "Programmable", "Programmer", "in", "tools", "Prolog", "Pseudocode",
             "Pseudolanguage", "Pseudo-operation", "Public", "PureBasic", "Push", "Python", "Q", "Qi", "QT",
             "Quick-and-dirty", "R", "Race", "condition", "Racket", "RAD", "Random", "seed", "RCS", "RDF", "Real",
             "number", "Recursion", "Recursive", "Regex", "Regular", "Reia", "Relational", "algebra", "Religion", "Chi",
             "REM", "Remark", "Repeat", "counter", "REPL", "word", "Resource", "Description", "Return", "Reverse",
             "engineering", "Revision", "ROM", "Routine", "Routing", "RPG", "Ruby", "Run", "time", "Rust", "S",
             "S-expression", "Safe", "font", "Sandbox", "Scala", "Scanf", "Schema", "matching", "Scheme", "Scratch",
             "SDK", "Second", "Section", "Security", "Descriptor", "Definition", "Segfault", "Separator", "Server",
             "side", "scripting", "Servlet", "SGML", "Shebang", "Shell", "scripts", "Short-circuit", "Signedness",
             "Simulated", "annealing", "Single", "step", "Smalltalk", "SMIL", "SOAP", "Socket", "Soft", "Software",
             "phases", "cycle", "Spaghetti", "Sparse", "Sparsity", "Special", "purpose", "SPL", "Spooling", "SQL",
             "Stack", "Standard", "attribute", "Stdin", "Strong", "Stubroutine", "Stylesheet", "Subprogram",
             "Subroutine", "Subscript", "Substring", "Subversion", "Superclass", "Switch", "Syntactic", "sugar",
             "Syntax", "System", "Systems", "Engineer", "T", "Tail", "Tcl", "Tcl/Tk", "Ternary", "Third-generation",
             "Thunk", "Tk", "Token", "Transcompiler", "True", "Tuple", "Turbo", "Turing", "completeness", "U", "Unary",
             "Undefined", "Underflow", "test", "V", "Value", "VB", "VHDL", "VIM", "Visual", "Studio", "Void", "W",
             "WebGL", "While", "Whole", "WML", "Workspace", "X", "XHTML", "XML", "XNA", "XOR", "XOXO", "XSL", "XSLT",
             "Y", "Currently", "no", "listings", "Z", "Z-buffering", "Zombie"]


def calc_checksum(s):
    sum = 0
    for c in s:
        sum += ord(c)
    sum = -(sum % 256)
    return '%2X' % (sum & 0xFF)


def compare(a, b, tmp, REQUEST):
    len_a = len(a)
    len_b = len(b)
    chs_a = calc_checksum(a)
    chs_b = calc_checksum(b)
    if (len_a != len_b) or (chs_a != chs_b):
        print("Maybe interesting " + REQUEST + " ---> " + str(tmp).lower() + " parameters")
    else:
        return 0


def create_get_request(get_url, params, get_value):
    if (len(params)) > 0:
        params = params.lower() + "=" + get_value
    ret = requests.get(get_url, params=params)
    return ret


def create_post_request(post_url, params, post_value):
    if (len(params)) > 0:
        params = params.lower() + "=" + post_value
    ret = requests.post(post_url, data=params)
    return ret


default_value = ["STRING", "False", "1337"]
url = "http://localhost/index.php"

for tmp_str in word_list:
    try:
        for value in default_value:
            # GET
            a = create_get_request(url, tmp_str, value)
            b = create_get_request(url, "", value)

            if a.status_code != b.status_code:
                a = create_get_request(url, tmp_str, value)
                b = create_get_request(url, "", value)
                if a.status_code != b.status_code:
                    print("Maybe interesting GET request " + str(tmp_str).lower())
                    print("F1 request " + str(a.status_code))
                    print("F2 request " + str(b.status_code))
            compare(a.text, b.text, tmp_str, "GET")

            # POST
            a = create_post_request(url, tmp_str, value)
            b = create_post_request(url, "", value)

            if a.status_code != b.status_code:
                a = create_post_request(url, tmp_str, value)
                b = create_post_request(url, "", value)
                if a.status_code != b.status_code:
                    print("Maybe interesting POST request " + str(tmp_str).lower())
                    print("F1 request " + str(a.status_code))
                    print("F2 request " + str(b.status_code))
            compare(a.text, b.text, tmp_str, "POST")
    except Exception, ex:
        print("Ups " + ex.message)
