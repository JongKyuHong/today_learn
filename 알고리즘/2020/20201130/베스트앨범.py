from collections import defaultdict
from operator import itemgetter


def solution(genres, plays):
    album = defaultdict(int)
    for a,b in zip(genres,plays):
        album[a] += b
    genre_rank = [genre for genre,play in sorted(album.items(),key = itemgetter(1),reverse=True)]
    final_dict = defaultdict(lambda : [])
    for i, genre_play_tuple in enumerate(zip(genres,plays)):
        final_dict[genre_play_tuple[0]].append((genre_play_tuple[1],i))
    answer = []

    for genre in genre_rank:
        one_genre_list = sorted(final_dict[genre],key=itemgetter(0),reverse=True)
        if len(one_genre_list) > 1:
            answer.append(one_genre_list[0][1])
            answer.append(one_genre_list[1][1])
        else:
            answer.append(one_genre_list[0][1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500,600,150,800,2500]))