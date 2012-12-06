#For this problem, use the same data set as in the previous problem. Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
print   reduce( lambda x, y: [x[0]+y[0]*(y[1]+x[1]), x[1]+y[1]], 
                sorted(
                    [map(int, job.split(' ')) 
                            for job in 
                                open('jobs.txt', 'r').read().split('\n')[1:-1]], 
                    key=lambda x: float(x[0])/x[1], 
                    reverse = True), 
                [0,0])[0]


