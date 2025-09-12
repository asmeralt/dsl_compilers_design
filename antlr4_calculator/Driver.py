import argparse
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ListenerInterp import ListenerInterp
from VisitorInterp import VisitorInterp


def main(args):
    input_stream = FileStream(args.file)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.start_()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
        return

    if args.worker == "visitor":
        vinterp = VisitorInterp()
        vinterp.visit(tree)
    elif args.worker == "listener":
        linterp = ListenerInterp()
        walker = ParseTreeWalker()
        walker.walk(linterp, tree)
    else:
        print(f"Unknown worker {args.worker}")
        return


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser(prog="ANTLR example script")
    args_parser.add_argument("--file", type=str)
    args_parser.add_argument("--worker", choices=["listener", "visitor"])
    args = args_parser.parse_args()

    main(args)
