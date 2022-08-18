import csv


def seed_csv_with_heading():
    file = open('movies.csv', mode = 'w', newline = '')
    csv_writer = csv.writer(file)

    csv_writer.writerow(['Title', 'Movie Year', 'Certificate','Rating', 'Duration', 'Total Ratings'])



def add_movie_to_csv(movie_obj):
    file = open('movies.csv', mode = 'a', newline = '')
    csv_writer = csv.writer(file)

    csv_writer.writerow([movie_obj.title, movie_obj.movie_year, movie_obj.certificate, movie_obj.rating, movie_obj.duration, movie_obj.total_ratings])
