import csv

df1 = []

df2 = []

df3 = []



with open('movies.csv') as m:

    csv_reading = csv.reader(m)

    data = list(csv_reading)

    all_movies = data[1:]

    headers = data[0]

headers.append("poster_link")

with open('final.csv', 'a+') as f:
    
    csv_writer = csv.writer(f)

    csv_writer.writerow(headers)

with open('poster.csv') as p:

    csv_reader = csv.reader(p)

    data = list(csv_reader)

    all_movies_links = data[1:]

for movie_item in all_movies:

    poster_found = any(movie_item[8] in movie_link_item for movie_link_item in all_movies_links)

    if (poster_found):

        for movie_link_item in all_movies_links:
        
            if (movie_item[8] == movie_link_item[0]):
        
                movie_item.append(movie_link_item[1])

                if (len(movie_item) == 28):
                   
                    with open('final.csv', 'a+') as f:

                        csv_writer = csv.writer(f)

                        csv_writer.writerow(movie_item)