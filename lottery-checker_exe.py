### Modifications for Distribution
# Ln 18,

import pandas as pd
from get_winning_superlotto import get_winning_superlotto_numbers

def check_lottery_numbers(ticket_numbers, input_numbers, winning_numbers):
    matching_numbers = sum(num in ticket_numbers[:-1] for num in input_numbers[:-1])
    matching_mega = input_numbers[-1] == ticket_numbers[-1]

    if matching_numbers >= 3 or matching_mega:
        winning_numbers.append(ticket_numbers)

    return matching_numbers, matching_mega

def main():
    # Load your CSV sheet into a pandas DataFrame
    ### ./_internal for distribution: './_internal/superlottoplustix.csv'
    csv_file_path = './superlottoplustix.csv'
    df = pd.read_csv(csv_file_path)

    # Get user input for lottery numbers
    winning_numbers, draw_date = get_winning_superlotto_numbers()
    print(f"The winning numbers from {draw_date} are:\n{winning_numbers}")

    # Iterate through each row in the csv
    print('')
    winning_tickets = []
    total_prize = 0

    for index, row in df.iterrows():
        # Extract the numbers from the current row
        ticket_numbers = row.tolist()

        # Check for matching numbers and mega numbers
        matching_numbers, matching_mega = check_lottery_numbers(ticket_numbers, winning_numbers, winning_tickets)

        # Print the results for the current row
        result_message = ""
        if matching_numbers >= 3 or matching_mega:
            result_message += "*** "

        result_message += f"Ticket {str(index + 1).zfill(2)}: {matching_numbers} matching numbers, {'Matching Mega' if matching_mega else 'No Matching Mega'}"
        print(result_message)

        # Calculate SuperLotto winnings for this ticket
        if matching_numbers == 0 and matching_mega:
            total_prize += 1
        elif matching_numbers == 1 and matching_mega:
            total_prize += 2
        elif matching_numbers == 2 and matching_mega:
            total_prize += 10
        elif matching_numbers == 3:
            if matching_mega:
                total_prize += 50
            else:
                total_prize += 8
        elif matching_numbers == 4:
            if matching_mega:
                total_prize += 1009
            else: 
                total_prize += 74
        elif matching_numbers == 5:
            if matching_mega :
                total_prize += 11000000
            else:
                total_prize += 11440
        else:
            pass
    
    if winning_tickets:
        print("\nWinning Numbers:")
        for winning_ticket in winning_tickets:
            print(winning_ticket)
        print(f"You've won ${total_prize}!")

    input("\n\nPress Enter to exit...")

if __name__ == "__main__":
    main()