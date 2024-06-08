from custom_checkers.custom_checker import PrintAndShowChecker


def register(linter):
    linter.register_checker(PrintAndShowChecker(linter))
