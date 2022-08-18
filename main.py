from csv_op import add_movie_to_csv, seed_csv_with_heading
from settings.error import Error
from utils import get_movie_data, print_movie_data, search_movie

seed_csv_with_heading()

def main():
    movie_path = search_movie()

    new_movie = get_movie_data(movie_path)

    add_movie_to_csv(new_movie)

    print_movie_data(new_movie)

    while True:

        try:
            key = input('Enter 1 to search another movie and 0 to exit : ')
            if not key.isdigit():
                raise TypeError(Error.TYPE_ERROR.value)

            if not int(key) == 1 and not int(key) == 0:
                raise ValueError(Error.VALUE_ERROR.value)

            if int(key) == 0: exit()
            else: main()
        
        except TypeError as error: 
            print(str(error))

        except ValueError as error: 
            print(str(error))


if __name__ == '__main__':
    main()
