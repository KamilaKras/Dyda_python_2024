import pandas as pd


def load_dataframe():
    # Define the correct column names based on the initial descriptive row
    column_names = ['Year', 'Length', 'Title', 'Subject', 'Actor', 'Actress', 'Director', 'Popularity', 'Awards',
                    '*Image']

    # Read data from CSV file skipping the first row and setting the correct column names
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1", skiprows=1, names=column_names)

    # Convert necessary columns to numeric
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df['Length'] = pd.to_numeric(df['Length'], errors='coerce')
    df['Popularity'] = pd.to_numeric(df['Popularity'], errors='coerce')

    return df


def task_1(df):
   #Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas, a następnie wyświetli wszystkie filmy z roku 2000
    return df[df['Year'] == 2000]


def task_2(df):
    #Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas, obliczy i wyświetli średnią długość filmów wszystkich reżyserów
    return df.groupby('Director')['Length'].mean()


def task_3(df):
    #Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas, utworzy nowy plik CSV zawierający tylko kolumny z tytułem, reżyserem i popularnością dla każdego filmu oraz zapisze go pod nową nazwą.
    selected_columns = df[['Title', 'Director', 'Popularity']]
    new_file_path = 'C:\\Users\\kamil\\PycharmProjects\\Pandas\\movies_selected_columns.csv'
    selected_columns.to_csv(new_file_path, index=False)
    return new_file_path


def task_4(df):
    #Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas, obliczy i wyświetli procentowy udział filmów z nagrodami w stosunku do całkowitej liczby filmów
    awards_count = df['Awards'].value_counts(normalize=True) * 100
    return awards_count.get('Yes', 0)  # Get 'Yes' percentage, default to 0 if not present

def task_5(df):
    #Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas, a następnie wyświetli wszystkie filmy z reżyserem o nazwisku "Kubrick".
    return df[df['Director'].str.strip().str.lower().str.contains('kubrick', na=False)]



def task_6(df):
   #Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas, obliczy i wyświetli sumę popularności filmów z gatunkiem "comedy".
    comedy_movies = df[df['Subject'].str.lower() == 'comedy']
    return comedy_movies['Popularity'].sum()


# Usage
df = load_dataframe()
print(task_1(df))
print(task_2(df))
file_path = task_3(df)
print(f'New CSV file saved at: {file_path}')
print(f'Percentage of movies with awards: {task_4(df)}%')
print(task_5(df))
print(f'Total popularity of comedy movies: {task_6(df)}')
