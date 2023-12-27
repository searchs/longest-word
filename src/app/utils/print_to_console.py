"""Print details e.g. customer record, to the console in formatted view"""
from loguru import logger


def console_card_printer(passenger, seat, flight_number, aircraft) -> str:
    output = (
        f"| Name: {passenger} |"
        f" Flight: {flight_number} |"
        f" Seat: {seat} |"
        f" Aircraft: {aircraft}"
        " |"
    )
    banner = "+" + "*" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"

    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    logger.info(f"\n{card}")
    return card


def console_words(matching_words, counts) -> str:
    output = f"| Matching: {matching_words} |" f" Counts: {counts}" " |"
    banner = "+" + "*" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"

    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    logger.info(f"\n{card}")
    return card
