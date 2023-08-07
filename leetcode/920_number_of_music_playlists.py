# n: number of different songs you have
# goal: how many songs you want on your playlist
# k: song can only be replayed if k other songs have been played

MODULO = 10 ** 9 + 7

def num_music_playlists(n, goal, k):
    dp = [[0] * (n + 1) for _ in range(goal + 1)]
    dp[0][0] = 1

    for playlist_length in range(1, goal + 1):
        for unique_songs in range(1, min(playlist_length, n) + 1):
            dp[playlist_length][unique_songs] = dp[playlist_length - 1][unique_songs - 1] * (n - unique_songs + 1) % MODULO
            if unique_songs > k:
                dp[playlist_length][unique_songs] = (dp[playlist_length][unique_songs] + dp[playlist_length - 1][unique_songs] * (unique_songs - k)) % MODULO
    
    return dp[-1][-1]