rank1 = float(input('How much did you score in the first test? '))
rank2 = float(input('How much did you score in the second test? '))
avg_rank = (rank1 + rank2) / 2

if avg_rank < 5:
    print('Average: {:.2f}'.format(avg_rank))
    print('Reproved!')
elif avg_rank >= 5 and avg_rank <= 6.9:
    print('Average: {:.2f}'.format(avg_rank))
    print('Catch-up!')
elif avg_rank >= 7:
    print('Average: {:.2f}'.format(avg_rank))
    print('Approved!')