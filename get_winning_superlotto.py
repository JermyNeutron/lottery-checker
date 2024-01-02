import requests
from bs4 import BeautifulSoup

def get_winning_superlotto_numbers():
    url = 'https://www.calottery.com/draw-games/superlotto-plus'
    response = requests.get(url)

    # Create variables
    winning_numbers = []
    draw_date = ''

    # Specify which html tags to target
    ul_target = "draw-cards--winning-numbers"
    span_target = "draw-cards--winning-numbers-inner-wrapper"
    date_target = "draw-cards--draw-date"

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <ul> tag with class "draw-cards--winning-numbers"
        ul_tag = soup.find('ul', class_=ul_target)

        if ul_tag:
            # Extract the list items (li) from the <ul> tag
            span_tags = ul_tag.find_all('span', class_=span_target)

            # Append the text content of each <span> tag to the winning_numbers
            winning_numbers.extend(int(span.text.strip()) for span in span_tags)

        else:
            print(f"No <ul> tag with class \"{ul_tag}\" found.")

        # Find the <p> tag with class "draw-cards--draw-date"
        date_tag = soup.find('p', class_=date_target)

        if date_tag:
            # Get the text content of the <p> tag
            draw_date = date_tag.text.strip()
        else:
            print(f"No <p> tag with class \"{date_tag}\" found.")

    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}.")

    return winning_numbers, draw_date

# For testing purposes below
# if __name__ == "__main__":
#     numbers, date = get_winning_superlotto_numbers()
#     print("Winning Numbers: ", numbers)
#     print("Draw Date:", date)