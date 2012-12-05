#Question 1
#In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times.. Download the text file here. This file describes a set of jobs with positive and integral weights and lengths. It has the format
#[number_of_jobs]
#[job_1_weight] [job_1_length]
#[job_2_weight] [job_2_length]
#...
#For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59. You should NOT assume that edge weights or lengths are distinct.
#
#Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

print   reduce( lambda x, y: [x[0]+y[0]*(y[1]+x[1]), x[1]+y[1]], 
                sorted(
                    [map(int, job.split(' ')) 
                            for job in 
                                open('jobs.txt', 'r').read().split('\n')[1:-1]], 
                    key=lambda x: [x[0]-x[1], x[0]], 
                    reverse = True), 
                [0,0])[0]

#f = open('jobs.txt', 'r')
#jobs = f.read()
#print jobs
#print len(jobs)
#print jobs.split('\n')
#print jobs.split('\n')[0:10]
#print jobs.split('\n')[-10:-1]
#print len(jobs.split('\n')[1:-1])


#jobs = jobs.split('\n')[1:4]
#jobs = jobs.split('\n')[1:-1]
#print jobs
#jobs = [map(int, job.split(' ')) for job in jobs]
#print jobs
#diff = [{int(job[0]) - int(job[1]): job}for job in jobs]
#diff = [{job[0] - job[1]: job}for job in jobs]
#diff.sort(reverse = True)
#print diff

#jobs.sort(key=lambda x: [x[0]-x[1], x[0]], reverse = True)
#print jobs
#jobs.sort(key=lambda x: x[0]-x[1], reverse = True)
#print jobs
#print reduce(lambda x, y: x+y[0]*y[1], jobs)
#print reduce(lambda x, y: x[0]*x[1]+y[0]*y[1], jobs)
#print reduce(lambda x, y: x+y[0]*y[1], jobs, 0)
#print reduce(lambda x, y: [x[0]+y[0]*(y[1]+x[1]), x[1]+y[1]], jobs, [0,0])
#a = 74*59
#print a
#b = (59+50)*8
#print a+b
#c = 74*59 + (59+73)*31+(59+73+50)*8
#print c 

#jobs = open('jobs.txt', 'r').read().split('\n')[1:4]
#jobs = [map(int, job.split(' ')) for job in open('jobs.txt', 'r').read().split('\n')[1:4]].sort(key=lambda x: [x[0]-x[1], x[0]], reverse = True)


