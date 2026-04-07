from RatingSystem import RatingSystem

class MySystem(RatingSystem):
    def __init__(self):
        super().__init__()
        self.movie_means = {}
        total_sum = 0
        total_count = 0
        
        for m_id, ratings in self.movie_ratings.items():
            self.movie_means[m_id] = sum(ratings) / len(ratings)
            total_sum += sum(ratings)
            total_count += len(ratings)
        
        self.global_mean = total_sum / total_count if total_count > 0 else 3.5

    def rate(self, user, movie):
        """
        Ta metoda zwraca rating w skali 1-5. Jest to ocena przyznana przez użytkownika 'user' filmowi 'movie'.
        """
        u_ratings = list(user.ratings.values())
        user_avg = sum(u_ratings) / len(u_ratings) if u_ratings else self.global_mean
        
        movie_avg = self.movie_means.get(movie, self.global_mean)
        prediction = (0.6 * user_avg) + (0.4 * movie_avg)
        
        return max(0.5, min(prediction, 5.0))

    def __str__(self):
        """
        Ta metoda zwraca numery indeksów wszystkich twórców rozwiązania. Poniżej przykład.
        """
        return 'System created by 155937, 155835 and 156014'
