from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class PrintAndShowChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = "print_and_show_checker"
    priority = -1
    msgs = {
        "C9999": (
            "print statement found: %s",
            "print-statement-warning",
            "Print statements should be avoided in production code.",
        ),
        "C9998": (
            "show method call found: %s",
            "show-method-warning",
            "Show method calls should be avoided in production code.",
        ),
    }

    def visit_call(self, node):
        """Called for function call nodes"""
        # Check for print statements
        if getattr(node.func, "name", None) == "print":
            self.add_message(
                "print-statement-warning", node=node, args=(node.as_string(),)
            )

        # Check for show method calls
        if getattr(node.func, "attrname", None) == "show":
            self.add_message("show-method-warning", node=node, args=(node.as_string(),))


def register(linter):
    """Required method to auto register this checker"""
    linter.register_checker(PrintAndShowChecker(linter))
