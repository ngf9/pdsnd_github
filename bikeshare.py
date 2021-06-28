import time
import pandas as pd
import numpy as np

city_filename = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTH_TO_NUMBER = {
    'january': 1,
    'february':2,
    'march':3,
    'april': 4,
    'may': 5,
    'june': 6
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('Which city would you like to explore: chicago, new york city or washington? \n> ').lower()
        if city in cities:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august']
    while True:
        month = input('Enter month to get that months result \n {} \n>'.format(months))
        if month in months:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
        day = input('Enter day to get result \n> {} \n> '.format(days))
        if day in days:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   
    file_name = city_filename[city]
    city_data = pd.read_csv(file_name)

    city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
    city_data['month'] = city_data['Start Time'].dt.month
    city_data['day_of_week'] = city_data['Start Time'].dt.weekday_name
    city_data['hour'] = city_data['Start Time'].dt.hour
    
    print(city_data.head())
    
    if month != "all":
        city_data = city_data[city_data.month == MONTH_TO_NUMBER[month]]
        
    print(city_data.head())
    
    return city_data


def time_stats(city_data):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
        
# TO DO: display the most common month
    common_month = city_data['month'].value_counts().idxmax()
    print('Most common month:\n', common_month)


    # TO DO: display the most common day of week
    
    common_day = city_data['day_of_week'].value_counts().idxmax()   
    print('Most common day of week:\n', common_day)


    # TO DO: display the most common start hour
    common_starthour = city_data['hour'].value_counts().idxmax()
    print('Most common start hour:\n', common_starthour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    city_data.head()

def station_stats(city_data):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    common_start_station = city_data['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", common_start_station)

    # TO DO: display most commonly used end station

    common_end_station = city_data['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
 
    city_data['Star_and_End'] = city_data['Start Station'] + " " + city_data['End Station']
    most_common_pair = city_data['Star_and_End'].value_counts().idxmax()
    print("The most frequent combination of start and end station trip :", most_common_pair)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(city_data):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = city_data['Trip Duration'].sum()
    print("The total travel time :", total_travel_time, "seconds")


    # TO DO: display mean travel time
    mean_travel_time = city_data['Trip Duration'].mean()
    print("The total travel time :", mean_travel_time, "seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city_data):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = city_data['User Type'].value_counts()
    print("The counts of user types: ", user_type_counts)

    print(city_data.head())
    
    # TO DO: Display counts of gender
    user_gender_counts = city_data['Gender'].value_counts()
    print("The counts of user genders: ", user_gender_counts)


    # TO DO: Display earliest, most recent, and most common year of birth
    user_YOB_earliest = city_data['Birth Year'].max()
    print("The earliest user year of birth: ", user_YOB_earliest)

    user_YOB_recent = city_data['Birth Year'].min()
    print("The most recent user year of birth: ", user_YOB_recent)
    
    user_YOB_common = city_data['Birth Year'].mode()
    print("The most common user year of birth: ", user_YOB_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        city_data = load_data(city, month, day)

        time_stats(city_data)
        station_stats(city_data)
        trip_duration_stats(city_data)
        user_stats(city_data)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
